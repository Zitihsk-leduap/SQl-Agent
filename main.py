from agent.sql_agent import create_sql_agent_instance

agent = create_sql_agent_instance()

while True:
    question = input("\nAsk a question (or type 'exit'): ")
    if question.lower() == "exit":
        break

    response = agent.invoke(question)
    print("\nAnswer:\n", response["output"])
