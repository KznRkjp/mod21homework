from django.http import HttpResponse
from django.shortcuts import render
from url_count.models import Url
from django.shortcuts import redirect

def index(request):
    return HttpResponse("Примитивный ответ из приложения tasks")


def url_list(request):
    all_urls = Url.objects.all()
    return render(
        request,
        'urls/list.html',
        {'urls': all_urls}
    )


def url_create(request):
    return render(request, "urls/create.html")

def add_url(request):
    if request.method == "POST":
        link = request.POST["URL"]
        search = request.POST["Search_string"]
        t = Url(url_link=link,word=search)
        t.save()
    return redirect("/urls/list/")
