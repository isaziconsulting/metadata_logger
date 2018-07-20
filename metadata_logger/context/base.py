import abc


class BaseMetadataContextManager(abc.ABC):
    @abc.abstractstaticmethod
    def get_metadata() -> dict:
        pass

    @abc.abstractstaticmethod
    def set_metadata(m: dict):
        pass
