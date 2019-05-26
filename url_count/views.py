from django.http import HttpResponse
from django.shortcuts import render
from url_count.models import Url
from django.shortcuts import redirect
from url_count.forms import AddUrlForm
def index(request):
    return HttpResponse("Примитивный ответ из приложения tasks")


def url_list(request):
    all_urls = Url.objects.all()
    return render(
        request,
        'urls/list.html',
        {'urls': all_urls},
        {"form": form}
    )


def url_create(request):
    return render(request, "urls/create.html")

# def add_url(request):
#     if request.method == "POST":
#         link = request.POST["URL"]
#         search = request.POST["Search_string"]
#         t = Url(url_link=link,word=search)
#         t.save()
#     return redirect("/url_count/list/")
def add_url(request):
    if request.method == "POST":
        form = AddUrlForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            url_link = cd["url_link"]
            word = cd['word']
            t = Url(url_link=url_link,word=word)
            t.save()
            return redirect("/url_count/list/")
    else:
        form = AddUrlForm()

    return render(request, "urls/list.html", {"form": form})
