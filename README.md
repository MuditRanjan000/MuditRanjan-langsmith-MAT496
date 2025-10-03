#### MODULE 1
### Video 1: Tracing Basics
* **What I Learned:** I learned how Langsmith captures traces by setting the `LANGCHAIN_TRACING_V2` environment variable. I also learned the critical importance of securely managing API keys. To resolve an `OpenAIError`, I set up a `.env` file to store my `OPENAI_API_KEY` and used the `python-dotenv` library to load it, ensuring my secrets are not hardcoded in the notebook.
* **My Code Tweak:** I created a chain using a `ChatPromptTemplate`, a `ChatOpenAI` model, and a `StrOutputParser` to generate a short story. The key fix was adding `load_dotenv()` to the top of my script and creating a `.gitignore` file to prevent my `.env` file from being committed to version control.
* **Source File:** [lesson_1.ipynb](my_learnings/module_1/lesson_1.ipynb)

### Video 2: Types of Runs
* **What I Learned:** I learned about the different "run types" in Langsmith (`llm`, `chain`, `tool`) and how they help organize traces. The key takeaway was using the `@traceable` decorator to create custom, nested traces for any function. This allows for granular visibility into custom application logic, not just default LangChain components.
* **My Code Tweak:** I created two functions, `process_query` and `summarize_query`. I decorated both with `@traceable`, making the first a "chain" and the second a "tool". I then called the parent function from the main script, which in turn called the child function. This successfully created a nested trace in Langsmith, clearly showing the parent-child relationship between the two custom runs.
* **Source File:** [lesson_2.ipynb](my_learnings/module_1/lesson_2.ipynb)
