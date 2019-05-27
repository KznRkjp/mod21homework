import time

from rq import Queue
from redis import Redis
import requests

def count_words_at_url(url):
    resp = requests.get(url)
    return len(resp.text.split())

urls = ["http://mail.ru","http://yandex.ru","http://google.com"]


reddis_conn=Redis()
q = Queue(connection=Redis())
for url in urls:
    job = q.enqueue(count_words_at_url, url)

while job.result is None:
    time.sleep(1)

print(job.result)
