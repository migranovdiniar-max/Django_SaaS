from django.contrib import admin
from django.urls import path

from cfehome.views import home_page_view

urlpatterns = [
    path("", home_page_view, name="home"),
    path("admin/", admin.site.urls),
]
