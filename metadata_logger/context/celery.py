"""
Metadata context manager for Celery.
It automatically copies metadata from the current task to the next task using a Celery signal.
"""
import logging

from celery import current_task, signals

from .. import manager
from .base import BaseMetadataContextManager
from .exceptions import ExecutedOutsideContext

_CELERY_X_HEADER = "x_sophia_celery_metadata"


logger = logging.getLogger(__name__)


def _is_in_context():
    if current_task._get_current_object() is None:
        raise ExecutedOutsideContext()


def _set_metadata_header(m: dict, headers: dict):
    headers[_CELERY_X_HEADER] = m


class CeleryMetadataContextManager(BaseMetadataContextManager):
    @staticmethod
    def get_metadata():
        _is_in_context()
        m = current_task.request.get(_CELERY_X_HEADER, {})
        return m

    @staticmethod
    def set_metadata(m: dict):
        _is_in_context()
        if not current_task.request.headers:
            current_task.request.headers = {}
        _set_metadata_header(m, current_task.request.headers)


def enable_context_metadata_propagation():
    """
    Will attach signal on celery application in order to propagate
    current context metadata to workers
    """
    manager.register_manager(CeleryMetadataContextManager)
    signals.before_task_publish.connect(
        _on_before_publish_insert_metadata_header)


def _on_before_publish_insert_metadata_header(headers, **kwargs):
    """
    This function is meant to be used as signal processor for "before_task_publish".
    :param Dict headers: The headers of the message
    :param kwargs: Any extra keyword arguments
    """
    if headers is None:
        logger.warning("HEADERS IS NONE: %s", headers)
        headers = {}
    _set_metadata_header(manager.metadata, headers)
