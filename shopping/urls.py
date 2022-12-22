from django.contrib.auth.decorators import login_required
from django.urls import path

from shopping.views import *

app_name = 'shopping'

urlpatterns = [
    path('', login_required(
        MainPage.as_view(),
        login_url='/accounts/login/'), name='home'),
    path('home/', login_required(
        MainPage.as_view(),
        login_url='/accounts/login/'), name='home'),
    path('home/<int:page>/', login_required(
        MainPage.as_view(),
        login_url='/accounts/login/'), name='home'),
    path('add_load/', login_required(
        AddLoad.as_view(),
        login_url='/accounts/login/'), name='add_load'),
    path('profile_of_load/<int:pk>/', login_required(
        ProfileOfLoad.as_view(),
        login_url='/accounts/login/'), name="profile_of_load"),
    path('delete_load/<int:pk>/', login_required(
        DeleteLoad.as_view(),
        login_url='/accounts/login/'), name='delete_load'),
    path('edit_load/<int:pk>/', login_required(
        EditLoad.as_view(),
        login_url='/accounts/login/'), name='edit_load'),
]
