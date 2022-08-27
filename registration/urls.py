from django.urls import path

from registration.views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('signup/', create_user, name='signup'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
]
