from django.urls import path

from registration.views import *

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLogin.as_view(), name='login'),
    path('signup/', CreateUser.as_view(), name='signup'),
    path('logout/', UserLogOut.as_view(), name='logout'),
    path('profile/', login_required(
        Profile.as_view(),
        login_url='/accounts/login/'
    ), name='profile'),
]
