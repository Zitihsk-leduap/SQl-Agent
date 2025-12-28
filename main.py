from agent.sql_agent import create_sql_agent

agent = create_sql_agent()

while True:
    question = input("\nAsk a question (or type 'exit'): ")
    if question.lower() == "exit":
        break

    for step in agent.stream(
        {"messages": [{"role": "user", "content": question}]},
        stream_mode="values",
    ):
        if "messages" in step:
            step["messages"][-1].pretty_print()
