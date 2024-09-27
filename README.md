This project implements the concept explored in the paper, "Can LLMs Generate Novel Research Ideas?", https://www.arxiv.org/abs/2409.04109 with some little twists.
This paper looks into using LLMs to generate future ideas from research papers.

In this project, the prompt given to the LLM is structured using the Diagram of Thought (DoT) framework, where the LLM acts as the Proposer, Critic, and Summarizer.
The Diagram of Thought (DoT) is a framework that models iterative reasoning in large language models (LLMs) as the construction of a directed acyclic graph (DAG) within a single model.

In the original paper of "Can LLMs Generate Novel Research Ideas", any section that hints at a future idea is striked off before presenting the research paper to the LLM.
The generated ideas are then validated by domain experts to ensure relevance and novelty.

In this implementation, the LLM independently handles the entire process:

- The Proposer generates the future research ideas.
- The Critic review these ideas to ensure they are relevant to the paper, novel, and feasible.
- The Summarizer synthesizes the remaining ideas and provides a concise summary for each one.

The results were better than I what envisioned, and this just shows the potential for LLMs to contribute to innovative research development.
After the process, I reviewed each idea and most times than not they were all relevant and novel. 
As for feasibility, it's challenging to judge without practical implementation—after all, in technology, nothing truly seems feasible until it’s achieved.
