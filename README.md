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

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#### MODULE 2

### Video 1: Datasets
* **What I Learned:** I learned how to programmatically create datasets in Langsmith using the SDK. The key steps are to initialize the `Client`, use `client.create_dataset()` to establish a new dataset with a name and description, and then use `client.create_examples()` with the `dataset_id` to upload examples in bulk.
* **My Code Tweak:** To demonstrate flexibility, I created a second dataset specifically for a summarization task. I defined a new schema with "article" as the input key and "summary" as the output key. This shows how to create datasets for various evaluation tasks beyond the standard question-and-answer format.
* **Source File:** [lesson_1.ipynb](my_learnings/module_2/lesson_1.ipynb)

### Video 2: Evaluators
* **What I Learned:** I learned the concepts of how to automate the evaluation process using the `run_on_dataset` function and `EvaluationConfig` object. The goal was to run a model against a dataset and apply both built-in and custom evaluators to score the results.
* **My Code Tweak & Issue:** I attempted to implement the lesson's code and a custom evaluator. However, I encountered a persistent `ImportError` for core evaluation functions like `run_on_dataset` and `EvaluationConfig`. This error persisted through exhaustive debugging, which included force-reinstalling libraries, creating a clean virtual environment with pinned dependencies from a `requirements.txt` file, re-registering the Jupyter kernel, and finally, attempting to run the code in a completely isolated Google Colab environment. The code is committed in its non-working state to document this unresolvable environment conflict.
* **Source File:** [lesson_2.ipynb](my_learnings/module_2/lesson_2.ipynb)

### Video 3: Experiments
* **What I Learned:** I learned the concept of using LangSmith Experiments to compare different models or prompts. The method involves running multiple evaluations against the same dataset and assigning them a shared `project_name` for side-by-side analysis in the UI.
* **My Code Tweak & Issue:** My goal was to create an experiment comparing `gpt-3.5-turbo` and `gpt-4o` on a summarization task. However, the code was blocked by the same persistent `ImportError` for `EvaluationConfig` from the previous lesson, confirming an unresolvable issue with the local environment.
* **Source File:** [lesson_3.ipynb](my_learnings/module_2/lesson_3.ipynb)
