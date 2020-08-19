from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
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
            messages.info(request,'password or username is not correct')
            return redirect('login')
        
    else:
        return render(request,'login.html')


def register(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        confirmPassword=request.POST['confirmPassword']
        
        

        if password1==confirmPassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"user taken")
                return redirect('register')
                #print("User with these username exists")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already exists")
                return redirect('register')
                #print("email already exists")
            else:    
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'Password doesnt match ,User not created')
            return redirect('register')
        return redirect("/")
    else:
        return render(request,'register.html')