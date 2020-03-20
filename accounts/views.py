from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.views.generic import TemplateView
from django.db import transaction
from django.contrib.auth.decorators import login_required

from accounts.forms import SignupForm, UserForm, ProfileForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    else:
        form = SignupForm()
        args = {'form': form}
    return render(request, 'accounts/signup.html', args)


class ProfileDetailView(TemplateView):
    template_name = 'accounts/my_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context.get('pk'):
            context['user'] = User.objects.get(pk=self.kwargs.get('pk'))
            return context
        else:
            context['user'] = self.request.user
        return context


@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('accounts:my_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })