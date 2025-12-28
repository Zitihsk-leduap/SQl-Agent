import pathlib, requests
from langchain_community.utilities import SQLDatabase

url = "https://storage.googleapis.com/benchmarks-artifacts/chinook/Chinook.db"
local_path = pathlib.Path("Chinook.db")

def get_database():
    if not local_path.exists():
        print("Downloading DB...")
        with open(local_path, "wb") as f:
            f.write(requests.get(url).content)
    else:
        print(f"DB already exists at {local_path.resolve()}")
    return SQLDatabase.from_uri(f"sqlite:///{local_path.resolve()}")
