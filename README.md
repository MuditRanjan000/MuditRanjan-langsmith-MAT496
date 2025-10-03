#### MODULE 1
### Video 1: Tracing Basics
* **What I Learned:** I learned how Langsmith captures traces by setting the `LANGCHAIN_TRACING_V2` environment variable. I also learned the critical importance of securely managing API keys. To resolve an `OpenAIError`, I set up a `.env` file to store my `OPENAI_API_KEY` and used the `python-dotenv` library to load it, ensuring my secrets are not hardcoded in the notebook.
* **My Code Tweak:** I created a chain using a `ChatPromptTemplate`, a `ChatOpenAI` model, and a `StrOutputParser` to generate a short story. The key fix was adding `load_dotenv()` to the top of my script and creating a `.gitignore` file to prevent my `.env` file from being committed to version control.
* **Source File:** [lesson_1.ipynb](my_learnings/module_1/lesson_1.ipynb)

### Video 2: Types of Runs
* **What I Learned:** I learned about the different "run types" in Langsmith (`llm`, `chain`, `tool`) and how they help organize traces. The key takeaway was using the `@traceable` decorator to create custom, nested traces for any function. This allows for granular visibility into custom application logic, not just default LangChain components.
* **My Code Tweak:** I created two functions, `process_query` and `summarize_query`. I decorated both with `@traceable`, making the first a "chain" and the second a "tool". I then called the parent function from the main script, which in turn called the child function. This successfully created a nested trace in Langsmith, clearly showing the parent-child relationship between the two custom runs.
* **Source File:** [lesson_2.ipynb](my_learnings/module_1/lesson_2.ipynb)

### Video 3: Alternative Ways to Trace
* **What I Learned:** I learned about alternative tracing methods beyond the `@traceable` decorator, specifically using `RunTree` for manual trace construction and the `traceable()` function as a context manager (`with traceable(...)`) for tracing arbitrary blocks of code like loops.
* **My Code Tweak & Issue:** I attempted to implement a custom tweak using the `with traceable()` context manager to wrap a `for` loop that made multiple LLM calls. However, this consistently resulted in a `TypeError: 'function' object does not support the context manager protocol`. We performed extensive debugging, including isolating the code in a new notebook, force-reinstalling all libraries, and creating a completely new, isolated virtual environment with its own Jupyter kernel. Despite these steps, the environment-specific error persisted. The code is committed as-is to document this issue.
* **Source File:** [lesson_3.ipynb](my_learnings/module_1/lesson_3.ipynb)

### Video 4: Conversational Threads
* **What I Learned:** I learned that Langsmith uses a `thread_ts` (timestamp/ID) to group otherwise independent runs into a single, continuous conversation. This is the mechanism that allows the UI to display threaded views for chatbots and agents, making it possible to trace an entire conversation's history.
* **My Code Tweak:** I simulated a two-turn conversation. I manually created a unique `conversation_id` and assigned it to the `thread_ts` field in the `extra` metadata for two separate `RunTree` objects. The first turn introduced a name, and the second asked the AI to recall it. In Langsmith, this correctly grouped the two runs into one thread, demonstrating the concept.
* **Source File:** [lesson_4.ipynb](my_learnings/module_1/lesson_4.ipynb)
