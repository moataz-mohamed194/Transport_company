from django.shortcuts import render
from django.views import View


class ErrorPage(View):
    template_name = 'error/error.html'

    def dispatch(self, request, *args, **kwargs):
        message = self.kwargs['message']
        return render(request, self.template_name, {'message': message})
