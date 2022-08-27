from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import Group, User
from registration.form import *
from django.contrib.auth import logout, login

from shopping.views import show_add_account


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            data_login = form.cleaned_data
            username = str(data_login['username'])
            password = str(data_login['password'])
            user = auth.authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('shopping:home')
        else:
            return redirect('error:error_page', 'check your data')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def create_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['repeatPassword']:
                if User.objects.filter(username=form.cleaned_data['userName']).count() < 1:
                    user = User.objects.create_user(username=form.cleaned_data['userName'],
                                                    password=form.cleaned_data['password'],
                                                    first_name=form.cleaned_data['first_name'])
                    if form.cleaned_data['is_admin']:
                        my_group = Group.objects.get(name='create_account')
                        my_group.user_set.add(user)
                    user.save()
                    return redirect('shopping:home')
                else:
                    return redirect('error:error_page', 'اسم الدخول مستخدم')
            else:
                return redirect('error:error_page', 'كلمة السر غير متطابقين')
        else:
            return redirect('error:error_page', 'تاكد من البيانات المدخلة')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('registration:login')


@login_required(login_url='/accounts/login/')
def profile(request):
    context = {
        'user': request.user.first_name,
        'create_account': show_add_account(request)
    }
    return render(request, 'registration/profile.html', context)
