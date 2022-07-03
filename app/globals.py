from redis import Redis  # type: ignore

r: Redis = Redis(host="localhost", port=6379, db=0)
