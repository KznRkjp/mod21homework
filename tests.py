import time

from rq import Queue
from redis import Redis
from test_func import count_words_at_url

urls = ["http://mail.ru","http://yandex.ru","http://google.com"]


redis_conn=Redis()
q = Queue(connection=redis_conn)
print("*"*85)
for url in urls:
    job = q.enqueue(count_words_at_url, url)
    while job.result is None:
        time.sleep(1)

    print(job.result)


#while job.result is None:
#    time.sleep(1)

#print(job.result)
