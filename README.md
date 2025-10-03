#### MODULE 1
### Video 1: Tracing Basics
* **What I Learned:** I learned how Langsmith captures traces by setting the `LANGCHAIN_TRACING_V2` environment variable. I also learned the critical importance of securely managing API keys. To resolve an `OpenAIError`, I set up a `.env` file to store my `OPENAI_API_KEY` and used the `python-dotenv` library to load it, ensuring my secrets are not hardcoded in the notebook.
* **My Code Tweak:** I created a chain using a `ChatPromptTemplate`, a `ChatOpenAI` model, and a `StrOutputParser` to generate a short story. The key fix was adding `load_dotenv()` to the top of my script and creating a `.gitignore` file to prevent my `.env` file from being committed to version control.
* **Source File:** [lesson_1.ipynb](my_learnings/module_1/lesson_1.ipynb)
