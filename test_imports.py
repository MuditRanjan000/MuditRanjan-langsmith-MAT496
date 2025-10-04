import sys
import os

print("--- Starting Local Environment Test ---")
print(f"Running from Python executable at:\n{sys.executable}\n")

if "langsmith_env" not in sys.executable:
    print("⚠️ WARNING: You are NOT running from the 'langsmith_env' virtual environment.")
    print("Please ensure you have activated it correctly before running this script.")

print("Attempting to import LangChain/LangSmith libraries...")
try:
    from langchain.smith import EvaluationConfig, run_on_dataset
    from langsmith.evaluation import LangChainStringEvaluator
    print("\n✅ SUCCESS: All libraries imported correctly!")
    print("This means your virtual environment is working. The problem is with Jupyter.")
except ImportError as e:
    print(f"\n❌ FAILED: Still encountered an ImportError.")
    print(f"   Error was: {e}")
    print("   This means the libraries are not installed correctly in this environment.")

print("\n--- Test Complete ---")