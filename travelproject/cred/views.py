from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def register(request):
    if request.method== 'POST':    #fetching data from form
        username=request.POST['username']
        firsname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']

        if password == cpassword:
            if User.objects.filter(username=username).exists():  # checking username correct or not
                messages.info(request, "username taken")
                return redirect('register')

            elif User.objects.filter(email=email).exists():  # checking username correct or not
                messages.info(request, "email taken")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password, first_name=firsname,
                                                last_name=lastname, email=email)
                user.save();
                return redirect('login')

        else:
            messages.info(request, 'password not matched')
            return redirect('register')
        print('user created')
        return redirect('/')
    return render(request, 'register.html')



def logout(request):
    auth.logout(request)
    return redirect('/')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    return render(request,'login.html')