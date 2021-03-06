"""
This type stub file was generated by pyright.
"""

from enum import Enum

red = ...
green = ...
yellow = ...
def read_config_file(module): # -> dict[str, Any]:
    """Reads all UPPERCASE variables de"""
    ...

def get_redis_from_config(settings, connection_class=...): # -> Redis[bytes] | Redis[Any] | Redis[str]:
    """Returns a StrictRedis instance f"""
    ...

def pad(s, pad_to_length):
    """Pads the given string to the giv"""
    ...

def get_scale(x): # -> int:
    """Finds the lowest scale where x <"""
    ...

def state_symbol(state): # -> str:
    ...

def show_queues(queues, raw, by_queue, queue_class, worker_class): # -> None:
    ...

def show_workers(queues, raw, by_queue, queue_class, worker_class): # -> None:
    ...

def show_both(queues, raw, by_queue, queue_class, worker_class): # -> None:
    ...

def refresh(interval, func, *args): # -> None:
    ...

def setup_loghandlers_from_args(verbose, quiet, date_format, log_format): # -> None:
    ...

def parse_function_arg(argument, arg_pos):
    class ParsingMode(Enum):
        ...
    
    

def parse_function_args(arguments): # -> tuple[list[Unknown], dict[Unknown, Unknown]]:
    ...

def parse_schedule(schedule_in, schedule_at): # -> datetime | None:
    ...

class CliConfig:
    """A helper class to be used with c"""
    def __init__(self, url=..., config=..., worker_class=..., job_class=..., queue_class=..., connection_class=..., path=..., *args, **kwargs) -> None:
        ...
    
    @property
    def connection(self): # -> Any | Redis[bytes] | Redis[Any] | Redis[str]:
        ...
    


