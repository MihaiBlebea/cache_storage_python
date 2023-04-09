import dropbox
from datetime import datetime, timedelta
import json
import os

from src.client_contract import ClientContract


class DropboxClient(ClientContract):
    def __init__(
        self, app_key: str = None, app_secret: str = None, refresh_token: str = None
    ) -> None:
        super().__init__()

        if app_key is None:
            app_key = os.getenv("DROPBOX_APP_KEY")

        if app_secret is None:
            app_secret = os.getenv("DROPBOX_APP_SECRET")

        assert isinstance(app_key, str), "app_key must be a string"
        assert isinstance(app_secret, str), "app_secret must be a string"

        self.app_key = app_key
        self.app_secret = app_secret

        self.dbx = dropbox.Dropbox(
            app_key="l6o3uw97luokkx5",
            app_secret="4v1rpadngy3o5vg",
            oauth2_refresh_token="ae386k6Xto4AAAAAAAAAASjKjkqHYVe98phQ0rTti9epsqcLLelBIlrGwJZhiqEV",
        )

    def _clean_path(self, path: str) -> str:
        if path[0] == ".":
            return path[1:]

        return path

    def download(self, path: str) -> dict:
        _, res = self.dbx.files_download(self._clean_path(path))

        return json.loads(res.content)

    def upload(self, path: str, data: dict = None) -> bool:
        mode = dropbox.files.WriteMode.overwrite

        self.dbx.files_upload(
            str.encode(json.dumps(data, indent=4, ensure_ascii=False)),
            self._clean_path(path),
            mode,
            mute=True,
        )

    def file_exists(self, path: str) -> bool:
        path = self._clean_path(path)
        folder = os.path.dirname(path)

        if folder == "/":
            folder = ""

        try:
            res = self.dbx.files_list_folder(folder)
            for f in res.entries:
                if f.path_display == path:
                    return True

            return False
        except:
            return False

    def last_modified(self, path: str) -> datetime:
        path = self._clean_path(path)
        folder = os.path.dirname(path)
        if folder == "/":
            folder = ""

        try:
            res = self.dbx.files_list_folder(folder)
            for f in res.entries:
                if f.path_display == path:
                    return f.server_modified + timedelta(hours=1)
        except:
            return None

    def create_folder_if_not_exists(self, folder_path: str) -> None:
        pass

    def authorize(self) -> None:
        auth = dropbox.DropboxOAuth2FlowNoRedirect(
            self.app_key, self.app_secret, token_access_type="offline"
        )

        redirect_url = auth.start()
        print("Please visit this link to authorize the app:\n" + redirect_url)

        code: str = input("Insert the code to authorize the application:\n")

        res = auth.finish(code.strip())

        print("Access token: " + res.access_token)
        print("Refreh token: " + res.refresh_token)
        print("Access token expires at: " + str(res.expires_at))


if __name__ == "__main__":
    DropboxClient("l6o3uw97luokkx5", "4v1rpadngy3o5vg").authorize()
