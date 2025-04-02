from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from home.models import Signup
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



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
   
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # Redirect to homepage after login
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'login.html')




def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Choose another one.")
            return redirect('signup')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, "Signup successful! You can now log in.")
        return redirect('login')  # Redirect to login page after signup

    return render(request, 'signup.html')




    #return render(request, 'login.html')