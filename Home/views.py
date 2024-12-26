from django.shortcuts import render, HttpResponse , redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from datetime import datetime
from Home.models import Contact

def home(request):
    return render(request, "HomeHtml/index.html")

def signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # Save the form, this will create the user
            user = form.save()

            # Get the cleaned data
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')

            # Send a registration email to the user
            htmly = get_template('gettingstart/welcome.html')
            d = {'username': username}
            subject = 'Welcome to Our Site'
            from_email = 'dronzer982@gmail.com'
            to = email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            # Display success message
            messages.success(request, f'Your account has been created! You are now able to log in.')

            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserRegisterForm()  # Render an empty form when the page is first accessed

    return render(request, "gettingstart/signup.html", {'form': form, 'title': 'Sign Up Here'})

def about(request):
    return render(request ,"aboutHtml/about.html")

def contact(request):
    if request.method == "POST":
        name  = request.POST.get('name')
        phone  = request.POST.get('phone')
        email  = request.POST.get('email')
        desc  = request.POST.get('desc')
        contact  = Contact(name=name,phone=phone,email=email,desc=desc,date=datetime.today())
        contact.save()   
    return render(request ,"contactHtml/contact.html")

def services(request):
    return render(request ,"servicesHtml/services.html")

# def login(request):
#     if request.method=="POST":
#         UserName =request.POST.get('UserName')
#         email =request.POST.get('email')
#         phone =request.POST.get('phone')
#         password =request.POST.get('password')
    
# def signup(request):
#     return render (request, "gettingstart/signup.html")

