from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import RedirectView

from shopping.form import *
from shopping.models import *


def show_add_account(request):
    if request.user.groups.filter(name='create_account').exists():
        return True
    else:
        return False


class MainPage(View):
    paginate_by = 10
    model = LoadData
    template_name = 'shopping/home.html'
    form_class = SearchForm

    def get(self, request):
        form = self.form_class
        context = {
            'form': form,
            'create_account': show_add_account(request)
        }
        return render(request, 'shopping/home.html', context)

    def post(self, request):

        form = self.form_class(request.POST)
        if form.is_valid():

            data = self.model.objects.all()
            if form.cleaned_data['number']:
                data = data.filter(number_of_car=form.cleaned_data['number'])

            if form.cleaned_data['get_in']:
                data = data.filter(date_of_get_in=form.cleaned_data['get_in'])

            if form.cleaned_data['get_out']:
                data = data.filter(date_of_get_out=form.cleaned_data['get_out'])

            if form.cleaned_data['load']:
                data = data.filter(load__regex=regex_transform(form.cleaned_data['load']))

            if form.cleaned_data['driver_name']:
                data = data.filter(driver__regex=regex_transform(form.cleaned_data['driver_name']))

            try:
                page = self.kwargs['page']
            except Exception as e:
                page = self.request.GET.get('page', 1)
            paginator = Paginator(data, self.paginate_by)
            users = paginator.page(page)

            context = {
                'form': form,
                'data': users,
                'create_account': show_add_account(request)
            }
        else:
            return redirect('error:error_page', 'تاكد من البيانات المدخلة')
        return render(request, self.template_name, context)


class AddLoad(View):
    model = LoadData
    template_name = 'shopping/add_load.html'
    form_class = AddForm

    def get(self, request):
        return render(request,
                      self.template_name,
                      {'form': self.form_class,
                       'create_account': show_add_account(request)})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            if form.cleaned_data["get_out"] < form.cleaned_data["get_in"]:
                context = {
                    'form': form,
                    'error': 'لا يجوز ان يكون تاريخ الخروج قبل التاريخ الدخول'
                }
                return render(request, 'shopping/add_load.html', context)

            data = LoadData(
                driver=form.cleaned_data["driver_name"],
                number_of_car=form.cleaned_data["number"],
                date_of_get_in=form.cleaned_data["get_in"],
                date_of_get_out=form.cleaned_data["get_out"],
                load=form.cleaned_data["load"],
                added_data=request.user.first_name,
            )
            data.save()
            return redirect('shopping:add_load')
        else:
            return redirect('error:error_page', 'تاكد من البيانات المدخلة')


class ProfileOfLoad(View):
    template_name = 'shopping/profile_load.html'
    model = LoadData

    def dispatch(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        data = self.model.objects.get(id=pk)
        print(data)
        return render(request,
                      self.template_name,
                      {'data': data,
                       'pk': pk,
                       'create_account': show_add_account(request)}
                      )


class DeleteLoad(View):
    model = LoadData

    def dispatch(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        data = self.model.objects.get(id=pk)
        data.delete()
        return redirect('shopping:home')


class EditLoad(RedirectView):
    template_name = 'shopping/edit_load.html'
    form_class = AddForm
    model = LoadData

    def get(self, request, *args, **kwargs):
        try:
            data = self.model.objects.get(id=self.kwargs['pk'])
        except:
            return render('error:error_page', 'هذه الحمولة غير مسجله')
        form_data = {
            'number': data.number_of_car,
            'load': data.load,
            'get_in': data.date_of_get_in,
            'get_out': data.date_of_get_out,
            'driver_name': data.driver
        }
        return render(request, self.template_name, {
            "form": self.form_class(form_data),
            'pk': self.kwargs['pk'],
            'create_account': show_add_account(request)
        })

    def post(self, request, *args, **kwargs):
        print(self.kwargs)
        try:
            data = self.model.objects.get(id=self.kwargs['pk'])
        except:
            return render('error:error_page', 'هذه الحمولة غير مسجله')
        form = self.form_class(request.POST)
        if form.is_valid():
            data.number_of_car = form.cleaned_data['number']
            data.load = form.cleaned_data['load']
            data.date_of_get_in = form.cleaned_data['get_in']
            data.date_of_get_out = form.cleaned_data['get_out']
            data.driver = form.cleaned_data['driver_name']
            data.edited_data = request.user.first_name
            data.save()
            return redirect('shopping:profile_of_load', self.kwargs['pk'])
        else:
            return redirect('error:error_page', 'برجاء التاكد من البيانات المدخله')
