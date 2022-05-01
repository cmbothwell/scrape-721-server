"""
This type stub file was generated by pyright.
"""

import click
from rq import __version__ as version
from rq.defaults import DEFAULT_JOB_MONITORING_INTERVAL, DEFAULT_LOGGING_DATE_FORMAT, DEFAULT_LOGGING_FORMAT, DEFAULT_RESULT_TTL, DEFAULT_WORKER_TTL

"""
RQ command line tool
"""
blue = ...
shared_options = ...
def pass_cli_config(func): # -> (*args: Unknown, **kwargs: Unknown) -> Any:
    ...

@click.group()
@click.version_option(version)
def main(): # -> None:
    """RQ command line tool."""
    ...

@main.command()
@click.option('--all', '-a', is_flag=True, help='Empty all queues')
@click.argument('queues', nargs=-1)
@pass_cli_config
def empty(cli_config, all, queues, serializer, **options): # -> None:
    """Empty given queues."""
    ...

@main.command()
@click.option('--all', '-a', is_flag=True, help='Requeue all failed jobs')
@click.option('--queue', required=True, type=str)
@click.argument('job_ids', nargs=-1)
@pass_cli_config
def requeue(cli_config, queue, all, job_class, serializer, job_ids, **options): # -> None:
    """Requeue failed jobs."""
    ...

@main.command()
@click.option('--interval', '-i', type=float, help='Updates stats every N seconds (d')
@click.option('--raw', '-r', is_flag=True, help='Print only the raw numbers, no b')
@click.option('--only-queues', '-Q', is_flag=True, help='Show only queue info')
@click.option('--only-workers', '-W', is_flag=True, help='Show only worker info')
@click.option('--by-queue', '-R', is_flag=True, help='Shows workers by queue')
@click.argument('queues', nargs=-1)
@pass_cli_config
def info(cli_config, interval, raw, only_queues, only_workers, by_queue, queues, **options):
    """RQ command-line monitor."""
    ...

@main.command()
@click.option('--burst', '-b', is_flag=True, help='Run in burst mode (quit after al')
@click.option('--logging_level', type=str, default="INFO", help='Set logging level')
@click.option('--log-format', type=str, default=DEFAULT_LOGGING_FORMAT, help='Set the format of the logs')
@click.option('--date-format', type=str, default=DEFAULT_LOGGING_DATE_FORMAT, help='Set the date format of the logs')
@click.option('--name', '-n', help='Specify a different name')
@click.option('--results-ttl', type=int, default=DEFAULT_RESULT_TTL, help='Default results timeout to be us')
@click.option('--worker-ttl', type=int, default=DEFAULT_WORKER_TTL, help='Default worker timeout to be use')
@click.option('--job-monitoring-interval', type=int, default=DEFAULT_JOB_MONITORING_INTERVAL, help='Default job monitoring interval ')
@click.option('--disable-job-desc-logging', is_flag=True, help='Turn off description logging.')
@click.option('--verbose', '-v', is_flag=True, help='Show more output')
@click.option('--quiet', '-q', is_flag=True, help='Show less output')
@click.option('--sentry-ca-certs', envvar='RQ_SENTRY_CA_CERTS', help='Path to CRT file for Sentry DSN')
@click.option('--sentry-debug', envvar='RQ_SENTRY_DEBUG', help='Enable debug')
@click.option('--sentry-dsn', envvar='RQ_SENTRY_DSN', help='Report exceptions to this Sentry')
@click.option('--exception-handler', help='Exception handler(s) to use', multiple=True)
@click.option('--pid', help='Write the process ID number to a')
@click.option('--disable-default-exception-hand', '-d', is_flag=True, help='Disable RQ\'s default exception ')
@click.option('--max-jobs', type=int, default=None, help='Maximum number of jobs to execut')
@click.option('--with-scheduler', '-s', is_flag=True, help='Run worker with scheduler')
@click.option('--serializer', '-S', default=None, help='Run worker with custom serialize')
@click.argument('queues', nargs=-1)
@pass_cli_config
def worker(cli_config, burst, logging_level, name, results_ttl, worker_ttl, job_monitoring_interval, disable_job_desc_logging, verbose, quiet, sentry_ca_certs, sentry_debug, sentry_dsn, exception_handler, pid, disable_default_exception_handler, max_jobs, with_scheduler, queues, log_format, date_format, serializer, **options):
    """Starts an RQ worker."""
    ...

@main.command()
@click.option('--duration', help='Seconds you want the workers to ', type=int)
@pass_cli_config
def suspend(cli_config, duration, **options): # -> None:
    """Suspends all workers, to resume """
    ...

@main.command()
@pass_cli_config
def resume(cli_config, **options): # -> None:
    """Resumes processing of queues, th"""
    ...

@main.command()
@click.option('--queue', '-q', help='The name of the queue.', default='default')
@click.option('--timeout', help='Specifies the maximum runtime of')
@click.option('--result-ttl', help='Specifies how long successful jo')
@click.option('--ttl', help='Specifies the maximum queued tim')
@click.option('--failure-ttl', help='Specifies how long failed jobs a')
@click.option('--description', help='Additional description of the jo')
@click.option('--depends-on', help='Specifies another job id that mu', multiple=True)
@click.option('--job-id', help='The id of this job')
@click.option('--at-front', is_flag=True, help='Will place the job at the front ')
@click.option('--retry-max', help='Maximum amount of retries', default=0, type=int)
@click.option('--retry-interval', help='Interval between retries in seco', multiple=True, type=int, default=[0])
@click.option('--schedule-in', help='Delay until the function is enqu')
@click.option('--schedule-at', help='Schedule job to be enqueued at a' 'timezone (e.g. 2021-05-27T21:45:')
@click.option('--quiet', is_flag=True, help='Only logs errors.')
@click.argument('function')
@click.argument('arguments', nargs=-1)
@pass_cli_config
def enqueue(cli_config, queue, timeout, result_ttl, ttl, failure_ttl, description, depends_on, job_id, at_front, retry_max, retry_interval, schedule_in, schedule_at, quiet, serializer, function, arguments, **options): # -> None:
    """Enqueues a job from the command """
    ...
