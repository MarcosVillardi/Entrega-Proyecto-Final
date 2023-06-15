from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("about/", views.info, name='about'),   
    path('login/', views.login_request, name="login"),
    path('logout/', LogoutView.as_view(template_name='home/logout.html'), name="logout"),
    path('register/', views.register_request, name="register"),

]
urlpatterns += staticfiles_urlpatterns()