from django.conf.urls import url
from django.contrib import admin
from . import views


app_name="info"

urlpatterns = [

  url(r"^$", views.InfoView.as_view(), name="info"),

]
