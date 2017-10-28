from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    if request.method == "POST":
        if(request.POST["password1"] == request.POST["password2"]):
            try:
                user = User.objects.get(username=request.POST["username"])
                return render(request, 'accounts/signup.html', {'error':'username already exists'})
            except:
                user = User.objects.create_user(request.POST["username"],password=request.POST["password1"])
                login(request, user)
                return render(request, 'accounts/signup.html')

        else:
            return render(request, 'accounts/signup.html', {'error':'passwords did not match'})
    else:
        return render(request, 'accounts/signup.html')

def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST["next"])
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'accounts/login_page.html', {'error': 'wrong username or password'})
    else:
        return render(request, 'accounts/login_page.html')

def logout_page(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')
