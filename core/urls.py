
from core.views import *
from django.urls import path

urlpatterns = [
path("",home,name="home"),
path("Contact/",contact,name="contact"),
path("Services/",services,name="services"),
path("About/",about,name="about"),
path("Portfolio/",portfolio,name="portfolio"),
path("Detail/",service_detail,name="service_detail"),
path("Process/",process,name="process"),
]
