from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import messages
from django.shortcuts import render, redirect
import uuid


def registerUser(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_obj = form.cleaned_data
            username = user_obj['username']
            email = user_obj['email']
            password = user_obj['password1']
            # user_obj = User.objects.create_user(username=username, email=email)
            # user_obj.set_password(password)
            profile_obj = Profile.objects.create(
                user=user_obj, auth_token=str(uuid.uuid4()))
            user_obj.save()

            return redirect('/token')
        else:
            context = {'form': form}
            messages.error(
                request, 'There is Error in your information...kindly refill the form')
            render(request, 'registration/signup.html', context)
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'home.html')


def success(request):
    return render(request, 'success.html')


def token_send(request):
    return render(request, 'token_send.html')
