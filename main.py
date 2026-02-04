from agents.planner import plan_task
from agents.executor import execute_task
from agents.verifier import verify_and_format

def run_ai_ops_assistant():
  print("Welcome to the AI Operations Assistant!")
  user_query = input("Please enter your query: ")

  # Step 1: Plan the task
  print("Planning the task...")
  decision = plan_task(user_query)
  print(f"Planned Decision: {decision}")

  # Step 2: Execute the task
  print("Executing the task...")
  raw_data = execute_task(decision, user_query)
  print(f"Raw Data: {raw_data}")

  # Step 3: Verify and format the results
  print("Verifying and formatting the results...")
  final_output = verify_and_format(raw_data, user_query)
  print("Final Output:")
  print(final_output)

if __name__ == "__main__":
  run_ai_ops_assistant()