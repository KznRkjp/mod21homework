# coding: utf-8
from django.core.management import BaseCommand
from datetime import datetime
from django.utils import timezone
from url_count.models import Url
import requests

class Command(BaseCommand):
    help = u"Display not yet completed tasks' dates"

    def add_arguments(self, parser):
        parser.add_argument('--warning-days', dest='warn_days', type=int, default=1)

    def handle(self, *args, **options):
        for t in Url.objects.filter(status=False):
            count = 0
            resp = requests.get(t.url_link)
            for i in resp.text.split():
                if i == t.word:
                    count += 1
            t.status = True
            t.result = count
            t.save()
            print(count)



        # now = datetime.now(timezone.utc)
        # for t in Url.objects.filter(status=False):
        #     if (now - t.date).days >= options['warn_days']:
        #         print("Старая задача:", t, t.date)
