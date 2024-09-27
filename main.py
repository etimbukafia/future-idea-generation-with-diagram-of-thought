import streamlit as st
import io
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from utils import Config
from pathlib import Path
from pydantic import BaseModel, Field
from langchain_core.output_parsers import JsonOutputParser

@st.cache_resource
def load_models():
    config = Config()
    config.initialize()
    return config.get_llm(), config.get_embeddings()

@st.cache_resource
def get_retriever():
    _, embeddings = load_models()
    vectorstore = Chroma(persist_directory="./research_papers_db", embedding_function=embeddings)
    return vectorstore.as_retriever()


def generate_ideas(input):
    llm, _ = load_models()
    retriever = get_retriever()
    folder_dir = Path.cwd() / "prompts"
    with io.open(folder_dir / "human_prompt.txt", "r", encoding="utf-8") as hp:
        human_prompt = hp.read()
    with io.open(folder_dir / "system_prompt.txt", "r", encoding="utf-8") as sp:
        system_prompt = sp.read()

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", human_prompt),
        ]
    )

    idea_generation_chain = create_stuff_documents_chain(llm, prompt)

    idea_retriever_chain = create_retrieval_chain(retriever, idea_generation_chain)

    response = idea_retriever_chain.invoke({"input": input})
    return response["answer"]



def main():
    st.title('Future Idea Generator')

    paper_title = st.text_input('Enter the title of the research paper you need ideas from')

    if st.button("Generate Ideas"):
        if not paper_title:
            st.error("Enter the title of the research paper")
        else:
            with st.spinner(f"Generating ideas from the paper: {paper_title}"):
                ideas = generate_ideas(paper_title)
                st.write(ideas)

if __name__ == "__main__":
    main()