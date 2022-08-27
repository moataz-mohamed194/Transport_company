from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from shopping.form import *
from shopping.models import *


def show_add_account(request):
    if request.user.groups.filter(name='create_account').exists():
        return True
    else:
        return False


@login_required(login_url='/accounts/login/')
def main_page(request, page=1):
    if request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            qd = request.GET
            data = LoadData.objects.all()
            if qd.get('number'):
                data = data.filter(number_of_car=qd.get('number'))

            if qd.get('get_in'):
                data = data.filter(date_of_get_in=qd.get('get_in'))

            if qd.get('get_out'):
                data = data.filter(date_of_get_out=qd.get('get_out'))

            if qd.get('load'):
                data = data.filter(load__regex=regex_transform(qd.get('load')))

            if qd.get('driver_name'):
                data = data.filter(driver__regex=regex_transform(qd.get('driver_name')))

            paginator = Paginator(data, 50)
            paginated_result = paginator.get_page(page)
            context = {
                'form': form,
                'data': paginated_result,
                'create_account': show_add_account(request)
            }
        else:
            return redirect('error:error_page', 'تاكد من البيانات المدخلة')
    else:
        form = SearchForm()
        context = {
            'form': form,
            'create_account': show_add_account(request)
        }
    return render(request, 'shopping/home.html', context)


@login_required(login_url='/accounts/login/')
def add_load(request):
    if request.POST:
        form = AddForm(request.POST)
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
    else:
        form = AddForm()
        context = {
            'form': form,
            'create_account': show_add_account(request)
        }
        return render(request, 'shopping/add_load.html', context)


@login_required(login_url='/accounts/login/')
def profile_of_load(request, pk):
    data = LoadData.objects.get(id=pk)
    context = {
        'data': data,
        'pk': pk,
        'create_account': show_add_account(request)
    }
    return render(request, 'shopping/profile_load.html', context)


@login_required(login_url='/accounts/login/')
def delete_load(request, pk):
    data = LoadData.objects.get(id=pk)
    data.delete()
    print(request)
    return redirect('shopping:home')


@login_required(login_url='/accounts/login/')
def edit_load(request, pk):
    try:
        data = LoadData.objects.get(id=pk)
    except:
        return render('error:error_page', 'هذه الحمولة غير مسجله')
    form_data = {
        'number': data.number_of_car,
        'load': data.load,
        'get_in': data.date_of_get_in,
        'get_out': data.date_of_get_out,
        'driver_name': data.driver
    }
    if request.POST:
        form = AddForm(request.POST)
        if form.is_valid():
            data.number_of_car = form.cleaned_data['number']
            data.load = form.cleaned_data['load']
            data.date_of_get_in = form.cleaned_data['get_in']
            data.date_of_get_out = form.cleaned_data['get_out']
            data.driver = form.cleaned_data['driver_name']
            data.edited_data = request.user.first_name
            data.save()
            return redirect('shopping:profile_of_load', pk)
        else:
            return redirect('error:error_page', 'برجاء التاكد من البيانات المدخله')
    else:
        form = AddForm(form_data)
        context = {
            "form": form,
            'pk': pk,
            'create_account': show_add_account(request)
        }
        return render(
            request, "shopping/edit_load.html", context)
