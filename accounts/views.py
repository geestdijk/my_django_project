from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.db import transaction
from django.contrib.auth.decorators import login_required

from accounts.forms import SignupForm, UserForm, ProfileForm
from file_upload_app.models import AvatarImage


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
            try:
                avatar = AvatarImage.objects.filter(
                    user=self.kwargs.get('pk')).order_by('-uploaded_at')[0]
            except IndexError:
                avatar = None
            context['avatar'] = avatar
            return context
        else:
            context['user'] = self.request.user

        print('===', context)

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


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'accounts/password_change.html'
    success_url = reverse_lazy('home')


class MyPasswordResetView(PasswordResetView):
    template_name = 'accounts/password_reset.html'
    success_url = reverse_lazy('home')
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'