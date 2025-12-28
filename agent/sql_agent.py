from agent.database import get_database
from agent.model import get_model
from langchain_community.agent_toolkits import SQLDatabaseToolkit       
from agent.prompt import get_system_prompt
from agent.tools import get_tools
from langchain.agents import create_agent



def create_sql_agent():
    model = get_model()
    db = get_database()
    tools = get_tools(db,model)
    prompt = get_system_prompt(db.dialect)


    agent = create_agent(
        model = model,
        tools = tools,
        system_prompt = prompt,
    )
    return agent

