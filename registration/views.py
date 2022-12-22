from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import Group, User
from django.utils.decorators import method_decorator
from django.views import View

from registration.form import *
from django.contrib.auth import logout, login

from shopping.views import show_add_account


class UserLogin(View):
    template_name = 'registration/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = auth.authenticate(
                username=str(form.cleaned_data['username']),
                password=str(form.cleaned_data['password']),
            )
            if user is not None:
                login(request, user)
                return redirect('shopping:home')
        return redirect('error:error_page', 'check your data')


class CreateUser(View):
    template_name = 'registration/signup.html'
    form_class = SignUpForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, context={'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
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


class UserLogOut(View):
    template_name = 'registration:login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect('registration:login')


class Profile(View):
    template_name = 'registration/profile.html'
    login_required = True

    def get(self, request):
        print(request.user)
        context = {
            'user': self.request.user.first_name,
            'create_account': show_add_account(self.request)
        }
        return render(request, 'registration/profile.html', context)
