from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("about/", views.info, name='about'),
]
urlpatterns += staticfiles_urlpatterns()