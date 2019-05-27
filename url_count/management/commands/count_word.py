# coding: utf-8
from django.core.management import BaseCommand
from datetime import datetime
from django.utils import timezone
from url_count.models import Url
import requests
from urllib.parse import urlparse
from rq import Queue
from redis import Redis
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
import test_func
import time

def check_url(url_link):
    validate = URLValidator(schemes=('http', 'https'))
    try:
        validate(url_link)
    except: #если не ок - пробуем подставить http://
        o = urlparse(url_link)
        if o.path:
            path = o.path
            while path.endswith('/'):
                path = path[:-1]
            path = "http://"+path
            validate(path)
            url_link = path
        else:
            url_link = "bad URL"
    return url_link

class Command(BaseCommand):
    help = u"Count how many times a word is found in the URL"

    def handle(self, *args, **options):
        job_list=[]
        redis_conn=Redis() #подключаем Редис
        q = Queue(connection=redis_conn) # и очередь

        for t in Url.objects.filter(status=False):

            check_url_result = check_url(t.url_link)
            if check_url_result == "bad URL":
                t.status = True
                t.result = "bad URL"
                t.last_update = datetime.now(timezone.utc)
                t.save()
                continue
            elif check_url_result != t.url_link:
                t.url_link = check_url_result
                t.save()

            job_list.append(str(t.job))
            jobs = q.enqueue(test_func.count_words_at_url,t.url_link,t.word,job_id=str(t.job))
        while len(job_list)>0:
            for task in job_list:
                job = q.fetch_job(task)
                while job.result is None:
                    time.sleep(1)
                obj = Class.objects.get(id=task)
                obj.result = job.result
                obj.status = True
                obj.last_update = datetime.now(timezone.utc)
                obj.save()
                job_list.remove(task)
