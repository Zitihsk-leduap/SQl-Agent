from langchain_community.agent_toolkits import SQLDatabaseToolkit
from agent.database import get_database
from agent.model import get_model


def get_tools(db,model):

    toolkit = SQLDatabaseToolkit(db = get_database(), llm = get_model())

    tools = toolkit.get_tools()
    return tools
