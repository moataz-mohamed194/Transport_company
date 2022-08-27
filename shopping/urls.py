from django.urls import path

from shopping.views import *

app_name = 'shopping'

urlpatterns = [
    path('', main_page, name='home'),
    path('home/', main_page, name='home'),
    path('home/<int:page>/', main_page, name='home'),
    path('add_load/', add_load, name='add_load'),
    path('profile_of_load/<int:pk>/', profile_of_load, name="profile_of_load"),
    path('delete_load/<int:pk>/', delete_load, name='delete_load'),
    path('edit_load/<int:pk>/', edit_load, name='edit_load'),
]
