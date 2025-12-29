import pathlib
from langchain_community.utilities import SQLDatabase

local_path = pathlib.Path("mydb.db")  # your local DB

def get_database():
    if not local_path.exists():
        print(f"Database {local_path} does not exist! Please create it first.")
        return None
    else:
        print(f"DB already exists at {local_path.resolve()}")
    return SQLDatabase.from_uri(f"sqlite:///{local_path.resolve()}")
