"""
Heavily inspired by https://github.com/Workable/flask-log-request-id
"""

from .base import BaseMetadataContextManager
from .exceptions import ExecutedOutsideContext


class MultiContextMetadataManager(object):
    """
    A class that can get and set Sophia metadata in different contexts such as Flask, Celery etc.
    """

    def __init__(self):
        self.ctx_managers = []
        self._metadata = {}

    def register_manager(self, ctx_manager: BaseMetadataContextManager):
        """
        Register another context-specialized manager
        :param Callable ctx_manager: A callable that will return the id or raise ExecutedOutsideContext if it was
         executed outside its context
        """
        if ctx_manager not in self.ctx_managers:
            self.ctx_managers.append(ctx_manager)

    @property
    def metadata(self) -> dict:
        for ctx_manager in self.ctx_managers:
            try:
                if not self._metadata:
                    self._metadata = ctx_manager.get_metadata() or {}
                return self._metadata
            except ExecutedOutsideContext:
                continue
        return {}

    @metadata.setter
    def metadata(self, m: dict):
        for ctx_manager in self.ctx_managers:
            try:
                new_metadata = {k: v for k, v in m.items() if v is not None}
                self._metadata = {**self.metadata, **new_metadata}
                return ctx_manager.set_metadata(self._metadata)
            except ExecutedOutsideContext:
                continue
