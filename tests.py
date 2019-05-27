import time
import sys
sys.path.append("/home/pi/skillfactory/mod21/mod21homework")
from rq import Queue
from redis import Redis
import test_func

urls = ["http://mail.ru","http://yandex.ru","http://google.com"]
test_func.count_words_at_url("http://mail.ru")

redis_conn=Redis()
q = Queue(connection=redis_conn)
print("*"*85)
for url in urls:
    job = q.enqueue(test_func.count_words_at_url, url)
while job.result is None:
    time.sleep(1)

print(job.result)


#while job.result is None:
#    time.sleep(1)

#print(job.result)
