import abc


class MethodNotImplemented(Exception):
    pass


class ClientContract(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def download(self, path: str):
        raise MethodNotImplemented()

    @abc.abstractmethod
    def upload(self, path: str, data: str = None):
        raise MethodNotImplemented()

    @abc.abstractmethod
    def file_exists(self, path: str):
        raise MethodNotImplemented()

    @abc.abstractmethod
    def last_modified(self, path: str):
        raise MethodNotImplemented()

    @abc.abstractmethod
    def create_folder_if_not_exists(self, folder_path: str) -> None:
        raise MethodNotImplemented()
