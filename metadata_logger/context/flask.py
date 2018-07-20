"""
Metadata context manager for Flask.
Automatically copies the current metadata from the Flask context to whatever other context is registered (e.g. Celery).
"""
from flask import _app_ctx_stack as stack
from flask import g

from metadata_logger import manager
from .base import BaseMetadataContextManager
from .exceptions import ExecutedOutsideContext

G_METADATA_ATTR = "x_sophia_flask_metadata"


def _is_in_context():
    if stack.top is None:
        raise ExecutedOutsideContext()


class FlaskMetadataContextManager(BaseMetadataContextManager):
    @staticmethod
    def get_metadata():
        _is_in_context()
        m = g.get(G_METADATA_ATTR, {})
        return m

    @staticmethod
    def set_metadata(m: dict):
        _is_in_context()
        setattr(g, G_METADATA_ATTR, m)


def init_metadata_logger():
    """
    Enables the Flask metadata context manager.
    """
    manager.register_manager(FlaskMetadataContextManager)
