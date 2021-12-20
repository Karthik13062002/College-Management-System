from django.shortcuts import redirect, render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def Courses(request):
    return render(request, 'courses.html')

def Contact(request):
    return render(request, 'contact.html')

def Login(request):
    return render(request, 'login.html')   

def Events(request):
    return render(request, 'events.html') 

def Fees(request):
    return render(request, 'fees.html')

def Registration(request):
    return render(request, 'registration.html')  
           

def handleSignup(request):
    if request.method == 'GET':

        first_name = request.GET['first_name']
        last_name = request.GET['last_name']
        email_id = request.GET['email']
        password = request.GET['password']
        confirmPassword = request.GET['confirmPassword']

        myuser = User.objects.create_user(email_id, first_name, last_name)
        myuser.save()
        messages.success(request, "SUCCESS")
        return redirect('Home')

    else:
        return HttpResponse('404 - NOT FOUND')

def Computer(request):
    return render(request, 'Computer.html')     

def Mechanical(request):
    return render(request, 'Mechanical.html')  
    
def Civil(request):
    return render(request, 'Civil.html') 

def Information(request):
    return render(request, 'Information.html') 

def AI(request):
    return render(request, 'AI.html')

def Data(request):
    return render(request, 'Data.html') 