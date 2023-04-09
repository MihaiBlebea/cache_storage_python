from pathlib import Path
from datetime import datetime
import json
import os

from src.client_contract import ClientContract


class LocalFileClient(ClientContract):
    def __init__(self) -> None:
        super().__init__()

    def download(self, path: str) -> dict:
        with open(path, "r") as file:
            return json.loads(file.read())

    def upload(self, path: str, data: dict = None) -> bool:
        with open(path, "w") as file:
            file.write(json.dumps(data, indent=4, ensure_ascii=False))

    def file_exists(self, path: str) -> bool:
        return os.path.isfile(path)

    def last_modified(self, path: str) -> datetime:
        return datetime.fromtimestamp(int(Path(path).stat().st_mtime))

    def create_folder_if_not_exists(self, folder_path: str) -> None:
        Path(folder_path).mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    c = LocalFileClient()
    print(c.last_modified("./src/__init__.py"))
