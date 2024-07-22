class HLDError(Exception):
    pass


class NotAnObjectError(HLDError):
    """Passed in object string does not match the object regex."""
