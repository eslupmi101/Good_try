from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect

from .models import Data
from .forms import Create_data
from .work_db import update_accomodation


User = get_user_model()


def index(request):
    template = 'basics/index.html'
    update_accomodation()
    data_list = Data.objects.all()
    paginator = Paginator(data_list, 10)
    data_number = request.GET.get('page')
    data_obj = paginator.get_page(data_number)
    context = {
        'title': "Главная страница",
        'page_obj': data_obj,
    }
    return render(request, template, context)


def data_detail(request, data_id):
    data = get_object_or_404(Data, pk=data_id)
    author = data.author
    number_data = Data.objects.filter(author=author).count()
    template = 'datas/data_detail.html'
    data_demo = data.text[:30]
    context = {
        'data': data,
        'data_demo': data_demo,
        'number_data': number_data,
    }
    return render(request, template, context)


def data_create(request):
    template = 'basics/create_data.html'
    if request.method == 'POST':
        form = Create_data(request.POST)
        if form.is_valid():
            post = Data()
            post.author = request.user
            post.description = form.cleaned_data['description']
            post.save()
            return redirect('basics:index')
    else:
        form = Create_data()
    return render(request, template, {'form': form})


def data_edit(request, data_id):
    template = 'basics/create_data.html'
    data = Data.objects.get(pk=data_id)
    is_edit = True
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Create_data(request.POST, instance=data)
        # check whether it's valid:
        if form.is_valid():
            if is_edit:
                data = Data()
            data.author = request.user
            data.description = form.cleaned_data['description']
            data.save()
            return redirect('basics:index')
    else:
        form = Create_data(instance=data)
    context = {
        'form': form,
        'is_edit': is_edit,
    }
    return render(request, template, context)
