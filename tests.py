import time
import sys
sys.path.append("/home/pi/skillfactory/mod21/mod21homework")
from rq import Queue
from redis import Redis
import test_func

urls = ["http://mail.ru","http://yandex.ru","http://google.com"]


redis_conn=Redis()
q = Queue(connection=redis_conn)
print("*"*85)
for url in urls:
    job = q.enqueue(test_func.count_words_at_url, url)

for job1 in q.jobs:
    while job1.result is None:
        time.sleep(1)
    print(job1.id, job1.result)



#while job.result is None:
#    time.sleep(1)

#print(job.result)
