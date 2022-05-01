"""
This type stub file was generated by pyright.
"""

class BaseRegistry:
    """
    Base implementation of a jo"""
    job_class = ...
    key_template = ...
    def __init__(self, name=..., connection=..., job_class=..., queue=..., serializer=...) -> None:
        ...
    
    def __len__(self):
        """Returns the number of jobs in th"""
        ...
    
    def __eq__(self, other) -> bool:
        ...
    
    def __contains__(self, item): # -> bool:
        """
        Returns a boolean indic"""
        ...
    
    @property
    def count(self):
        """Returns the number of jobs in th"""
        ...
    
    def add(self, job, ttl=..., pipeline=..., xx=...):
        """Adds a job to a registry with ex"""
        ...
    
    def remove(self, job, pipeline=..., delete_job=...):
        """Removes job from registry and de"""
        ...
    
    def get_expired_job_ids(self, timestamp=...): # -> list[str | None]:
        """Returns job ids whose score are """
        ...
    
    def get_job_ids(self, start=..., end=...): # -> list[str | None]:
        """Returns list of all job ids."""
        ...
    
    def get_queue(self): # -> Queue:
        """Returns Queue object associated """
        ...
    
    def get_expiration_time(self, job): # -> datetime:
        """Returns job's expiration time."""
        ...
    
    def requeue(self, job_or_id): # -> Job | Any:
        """Requeues the job with the given """
        ...
    


class StartedJobRegistry(BaseRegistry):
    """
    Registry of currently execu"""
    key_template = ...
    def cleanup(self, timestamp=...): # -> list[str | None]:
        """Remove expired jobs from registr"""
        ...
    


class FinishedJobRegistry(BaseRegistry):
    """
    Registry of jobs that have """
    key_template = ...
    def cleanup(self, timestamp=...): # -> None:
        """Remove expired jobs from registr"""
        ...
    


class FailedJobRegistry(BaseRegistry):
    """
    Registry of containing fail"""
    key_template = ...
    def cleanup(self, timestamp=...): # -> None:
        """Remove expired jobs from registr"""
        ...
    
    def add(self, job, ttl=..., exc_string=..., pipeline=...): # -> None:
        """
        Adds a job to a registr"""
        ...
    


class DeferredJobRegistry(BaseRegistry):
    """
    Registry of deferred jobs ("""
    key_template = ...
    def cleanup(self): # -> None:
        """This method is only here to prev"""
        ...
    


class ScheduledJobRegistry(BaseRegistry):
    """
    Registry of scheduled jobs."""
    key_template = ...
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def schedule(self, job, scheduled_datetime, pipeline=...):
        """
        Adds job to registry, s"""
        ...
    
    def cleanup(self): # -> None:
        """This method is only here to prev"""
        ...
    
    def remove_jobs(self, timestamp=..., pipeline=...):
        """Remove jobs whose timestamp is i"""
        ...
    
    def get_jobs_to_schedule(self, timestamp=..., chunk_size=...): # -> list[str | None]:
        """Remove jobs whose timestamp is i"""
        ...
    
    def get_scheduled_time(self, job_or_id): # -> datetime:
        """Returns datetime (UTC) at which """
        ...
    


class CanceledJobRegistry(BaseRegistry):
    key_template = ...
    def get_expired_job_ids(self, timestamp=...):
        ...
    
    def cleanup(self): # -> None:
        """This method is only here to prev"""
        ...
    


def clean_registries(queue): # -> None:
    """Cleans StartedJobRegistry, Finis"""
    ...
