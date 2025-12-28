from agent.database import get_database
from agent.model import get_model
from agent.prompt import get_system_prompt
from langchain_community.agent_toolkits import create_sql_agent


def create_sql_agent_instance():
    model = get_model()
    db = get_database()

    agent = create_sql_agent(
        llm=model,
        db=db,
        verbose=True,
        system_prompt=get_system_prompt(db.dialect),
    )

    return agent
