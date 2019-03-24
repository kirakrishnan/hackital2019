from django.shortcuts import render

# Create your views here.

from .models import User

from django.http import HttpResponse
from django.template import loader

# def index(request):
#     user_list = User.objects.order_by('name')
#     template = loader.get_termplate('streetparking/index.html')
#     context = {
#         'user_list': user_list,
#     }
#     # output = ','.join([u.name for u in user_list])
#     # return HttpResponse(output)
#     return HttpResponse(template.render(context,request))

def index(request):
    user_list = User.objects.order_by('name')
    context = {'user_list': user_list}
    return render(request, 'streetparking/index.html', context)


def detail(request):
    user_list = User.objects.all()
    context = {'user_list': user_list}
    return render(request, 'streetparking/details.html', context)
    # return HttpResponse("details of the user")

def results(request):
    return HttpResponse("results of the user")
