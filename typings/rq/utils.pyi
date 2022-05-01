"""
This type stub file was generated by pyright.
"""

import logging

"""
Miscellaneous helper functions."""
class _Colorizer:
    def __init__(self) -> None:
        ...
    
    def reset_color(self):
        ...
    
    def colorize(self, color_key, text):
        ...
    


colorizer = ...
def make_colorizer(color): # -> (text: Unknown) -> Unknown:
    """Creates a function that colorize"""
    ...

class ColorizingStreamHandler(logging.StreamHandler):
    levels = ...
    def __init__(self, exclude=..., *args, **kwargs) -> None:
        ...
    
    @property
    def is_tty(self): # -> Any | None:
        ...
    
    def format(self, record): # -> str:
        ...
    


def import_attribute(name): # -> Any:
    """Return an attribute from a dotte"""
    ...

def utcnow(): # -> datetime:
    ...

_TIMESTAMP_FORMAT = ...
def utcformat(dt):
    ...

def utcparse(string): # -> datetime:
    ...

def first(iterable, default=..., key=...): # -> None:
    """
    Return first element of `it"""
    ...

def is_nonstring_iterable(obj): # -> bool:
    """Returns whether the obj is an it"""
    ...

def ensure_list(obj): # -> list[Unknown]:
    """
    When passed an iterable of """
    ...

def current_timestamp(): # -> int:
    """Returns current UTC timestamp"""
    ...

def backend_class(holder, default_name, override=...): # -> Any:
    """Get a backend class using its de"""
    ...

def str_to_date(date_str): # -> datetime | None:
    ...

def parse_timeout(timeout): # -> int | Integral:
    """Transfer all kinds of timeout fo"""
    ...

def get_version(connection): # -> tuple[int, ...] | tuple[Literal[5], Literal[0], Literal[9]]:
    """
    Returns tuple of Redis serv"""
    ...

def ceildiv(a, b):
    """Ceiling division. Returns the ce"""
    ...

def split_list(a_list, segment_size): # -> Generator[Unknown, None, None]:
    """
    Splits a list into multiple"""
    ...

def truncate_long_string(data, max_length=...):
    """Truncate arguments with represen"""
    ...

def get_call_string(func_name, args, kwargs, max_length=...): # -> str | None:
    """Returns a string representation """
    ...
