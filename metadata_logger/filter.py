import logging

from metadata_logger import get_current_metadata


class MetadataLogFilter(logging.Filter):
    """
    Log filter to inject the current context metadata into the LogRecord
    """

    def filter(self, record: logging.LogRecord):
        metadata = get_current_metadata()
        assert isinstance(metadata, dict), "metadata must be a dict"
        if metadata:
            for k, v in metadata.items():
                setattr(record, k, v)
        return record
