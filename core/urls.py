
from core.views import *
from django.urls import path

urlpatterns = [
path("",home,name="home"),
path("Contact/",contact,name="contact"),
path("Services/",services,name="services"),
path("About/",about,name="about"),
path("Portfolio/",portfolio,name="portfolio"),
path("Process/",process,name="process"),
path("pe-stamp/",pe_stamp,name="pe_stamp"),
path("solar-permit-design/",solar_permit,name="solar_permit"),
path("solar-sales-proposal/",solar_sales,name="solar_sales"),
]
