class ExecutedOutsideContext(Exception):
    """
    Exception to be raised if a fetcher was called outside its context
    """
    pass
