from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("this is home page")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")

def services(request):
   return render(request, 'services.html')
   # return HttpResponse("This is services page")

def contact(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contact(firstname=firstname, lastname=lastname, email=email, message= message, date= datetime.today())
        contact.save()
        messages.success(request, "Your response submitted.")

    return render(request, 'contact.html')
   # return HttpResponse("this is contact page")