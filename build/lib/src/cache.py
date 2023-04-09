from datetime import timedelta, datetime
import os
from src.client_contract import ClientContract


class Cache:
    def __init__(self, client: ClientContract) -> None:
        self.client = client

    def cache_factory(self, cache_file_template: str, ttl_sec: int):
        assert isinstance(
            cache_file_template, str
        ), "cache_file_template must be a string type"
        assert isinstance(ttl_sec, int), "ttl_sec must be a int type"

        def cache(func):
            def wrapper(*args, **kwargs):
                if len(kwargs) > 0:
                    file_path = cache_file_template.format(**kwargs)
                elif len(args) > 0:
                    file_path = cache_file_template.format(args)
                else:
                    file_path = cache_file_template

                folder = os.path.dirname(file_path)

                self.client.create_folder_if_not_exists(folder)

                if self.client.file_exists(file_path):
                    created_at = self.client.last_modified(file_path)
                    if datetime.now() < created_at + timedelta(seconds=ttl_sec):
                        print(f"Fetching {file_path} from cache")

                        return self.client.download(file_path)

                print(f"Fetching {file_path} from source")
                result = func(*args, **kwargs)

                self.client.upload(file_path, result)

                return result

            return wrapper

        return cache
