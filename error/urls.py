from django.urls import path

from error.views import error_page

app_name = 'error'

urlpatterns = [
    path('error_page/<str:message>/', error_page, name='error_page'),
]
