# coding: utf-8
from django.core.management import BaseCommand
from datetime import datetime
from url_count.models import Url

class Command(BaseCommand):
    help = u"Display not yet completed tasks' dates"

    def add_arguments(self, parser):
        parser.add_argument('--warning-days', dest='warn_days', type=int, default=1)

    def handle(self, *args, **options):
        now = datetime.now(timezone.utc)
        for t in Url.objects.filter(status=False):
            if (now - t.date).days >= options['warn_days']:
                print("Старая задача:", t, t.created)
