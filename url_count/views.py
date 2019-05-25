from django.http import HttpResponse
from django.shortcuts import render
from url_count.models import Url

def index(request):
    return HttpResponse("Примитивный ответ из приложения tasks")


def url_list(request):
    all_tasks = Url.objects.all()
    return render(
        request,
        'urls/list.html',
        {'urls': all_urls}
    )
