"""
This module helps with automatically logging useful metadata, like company, unique_id etc.
It uses "Context Managers" to get and set the metadata, as different contexts exist depending on where the log
statement is called from. For example, Flask and Celery both have different context implementations, which are
abstracted away by this module.

It is very simple to use:
  initialise a `Metadata` instance
  call `set_current_metadata(metadata)`
  later, call `get_current_metadata()` to retrieve it.
"""

import logging

from .context import MultiContextMetadataManager

logger = logging.getLogger(__name__)


manager = MultiContextMetadataManager()
