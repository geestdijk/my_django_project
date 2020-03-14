from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from accounts.forms import UserForm, ProfileForm
from django.contrib import messages


def signup(request):
    if request.method =='POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect(reverse('accounts:home'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = RegistrationForm()
        profile_form = ProfileForm()

        args = {'user_form': user_form, 'profile_form': profile_form}
        return render(request, 'accounts/signup.html', args)