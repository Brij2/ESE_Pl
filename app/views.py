from django.shortcuts import render
from .models import Customer

# Create your views here.

def login(request) : 
    if request.POST : 
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        print(username)
        print(password)
        
        user = Customer.objects.filter(username = username).values().first()
        
        if user['password'] == password : 
            return render('app/home.html')
  
    return render(request,'app/login.html')