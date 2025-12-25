from django.contrib import admin
from django.urls import path

from cfehome.views import home_view, about_view
from auth import views as auth_views


urlpatterns = [
    path("", home_view, name="home"),
    path("login/", auth_views.login_view, name="login"),
    path("register/", auth_views.register_view, name="register"),
    path("about/", about_view, name="about"),
    path("admin/", admin.site.urls),
]
