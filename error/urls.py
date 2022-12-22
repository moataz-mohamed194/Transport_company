from django.urls import path

from error.views import ErrorPage

app_name = 'error'

urlpatterns = [
    path('error_page/<str:message>/', ErrorPage.as_view(), name='error_page'),
]
