from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('/')

    else:
        form = UserRegisterForm()

    return render(request, "sign_up.html", {'form': form})


@login_required
def profile(request, *args, **kwargs):
    if request.method == 'POST':
        update_form = UserUpdateForm(request.POST, instance=request.user)
        if update_form.is_valid():
            update_form.save()
            messages.success(request, f'Your profile has been updated')
            return redirect('/users/profile')
    else:
        update_form = UserUpdateForm(instance=request.user)

    context = {
        'form': update_form,
    }
    return render(request, 'profile.html', context)
