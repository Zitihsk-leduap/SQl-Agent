import pathlib, requests
from langchain_community.utilities import SQLDatabase

url = "https://storage.googleapis.com/benchmarks-artifacts/chinook/Chinook.db"

local_path = pathlib.Path("Chinook.db")


def get_database():
    if not local_path.exists():
        with open(local_path, "wb") as f:
            f.write(requests.get(url).content)
    return SQLDatabase.from_uri(f"sqlite:///{local_path}")