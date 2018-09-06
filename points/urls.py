from django.conf.urls import url
from django.contrib import admin
from . import views

app_name="points"

urlpatterns = [

  url(r"^$", views.PointView.as_view(), name="points"),

]
