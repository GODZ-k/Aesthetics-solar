
from core.views import *
from django.urls import path

urlpatterns = [
path("",home,name="home"),
path("contact/",contact,name="contact"),
path("services/",services,name="services"),
]
