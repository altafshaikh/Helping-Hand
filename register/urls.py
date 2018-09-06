from django.conf.urls import url
from django.contrib import admin
from . import views


app_name="register"

urlpatterns = [

  url(r"^$", views.Register, name="register"),

]
