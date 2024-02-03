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



# customer contact detail --------------------------------

def save_detail(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        user_form = user_data(name=name, email=email, phone=phone, subject=subject, message=message)
        user_form.save()

        return redirect("/contact/")
