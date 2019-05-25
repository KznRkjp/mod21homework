from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.url_list, name='list'),
    path("create/", views.url_create, name='create')
    path("add-url/", views.add_url, name="api-add-url"),
]
