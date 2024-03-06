from django.shortcuts import render,redirect
from core.models import *

# Create your views here.

def home(request):

   # customer contact detail --------------------------------
    save_detail(request)

    return render(request, 'index.html')


def contact(request):

    return render(request, 'contact.html')


def services(request):
    return render(request, 'service.html')


def about(request):
    return render(request, 'about.html')


def portfolio(request):
    return render(request, 'portfolio.html')

def process(request):
    return render(request, 'process.html')

def service_detail(request):
    return render(request, 'service_detail.html')
# customer contact detail --------------------------------

def pe_stamp(request):
    return render(request, 'pe-stamp.html')

def solar_permit(request):
    return render(request, 'solar-permit-design.html')

def solar_sales(request):
    return render(request, 'solar-sales-proposal.html')

def save_detail(request):
    if request.method == 'POST':
        try:
          name=request.POST.get('name')
          email=request.POST.get('email')
          phone=request.POST.get('phone')
          subject=request.POST.get('subject')
          message=request.POST.get('message')

          user_form = user_data(name=name, email=email, phone=phone, subject=subject, message=message)
          user_form.save()

        except Exception as e:

             print(e)


        return redirect("/contact/")
