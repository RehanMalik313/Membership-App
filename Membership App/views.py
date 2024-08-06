from django.shortcuts import render, redirect
from .models import Member
from .forms import Memberform
from django.contrib import messages


def home(request):
    all_members = Member.objects.all()
    return render(request, "home.html", {'all':all_members})

def join(request):
    if request.method == "POST":        
        form = Memberform(request.POST)
        if form.is_valid():
            form.save()
        else:
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            passw = request.POST['passw']
            age = request.POST['age']


            messages.success(request, ('Email already exists! Please Try again...'))
            #return redirect('join')
            return render(request, 'join.html',{'fname':fname,
            'lname':lname, 
            'email':email, 
            'passw':passw, 
            'age':age})    


        messages.success(request, ("You have successfully Signed Up"))
        return redirect('home')      
    else:
        return render(request, 'join.html',{})    
