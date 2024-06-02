from django.urls import path
from . import views #ata dia link kora hoise


urlpatterns = [
    path("courses/", views.courses),
    path("about/", views.about),
    path("", views.home),
]