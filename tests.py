import time

from rq import Queue
from redis import Redis

q = Queue(connection=Redis())
job = q.enqueue(len, ["Анна", "Мария", "Валентина"])

while job.result is None:
    time.sleep(1)

print(job.result) 
