from django.shortcuts import render


def error_page(request, message):
    return render(request, 'error/error.html', {'message': message})
