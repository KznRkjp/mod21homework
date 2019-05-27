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

class Command(BaseCommand):
    help = u"Count how many times a word is found in the URL"

    #def add_arguments(self, parser):
    #    parser.add_argument('--warning-days', dest='warn_days', type=int, default=1)

    def handle(self, *args, **options):
        for t in Url.objects.filter(status=False):

            count = 0

            validate = URLValidator(schemes=('http', 'https'))
            try:
                validate(t.url_link)
            except:
                o = urlparse.urlparse(t.url_link)
                if o.path:
                    path = o.path
                    while path.endswith('/'):
                        path = path[:-1]
                    path = "http://"+path
                    validate(path)
                    t.url_link = path
                    t.save
                else:
                    t.status = True
                    t.result = "bad URL"
                    t.last_update = datetime.now(timezone.utc)
                    t.save()
                    continue


            resp = requests.get(t.url_link)
            #print (resp.text)
            for i in resp.text.split():
                if i == t.word:
                    count += 1
            t.status = True
            t.result = count
            t.last_update = datetime.now(timezone.utc)
            t.save()
            print(t.url_link,t.word,t.result,t.last_update)



        # now = datetime.now(timezone.utc)
        # for t in Url.objects.filter(status=False):
        #     if (now - t.date).days >= options['warn_days']:
        #         print("Старая задача:", t, t.date)
