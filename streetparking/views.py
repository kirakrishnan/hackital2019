from django.shortcuts import render

# Create your views here.

from .models import User
from .twilio_message import MessageClient

from django.http import HttpResponse
from django.template import loader
import random
from datetime import datetime, timedelta

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
    mc = MessageClient()
    user_list = User.objects.all()
    plate_list = ["RK-099AN", "RK 340AO", "RK-115AN", "RK-248AH", "RK 346AL", "RK-892AE", "RK 019AF", "M 633BD"
        ,"RK 576AH", "BB 751BH", "RK-755AJ", "S1 819AK", "2T4 0211", "4BO 4979", "4B3 9376", "BSE55-79"]
    random_plate = random.choice(plate_list)
    random_time = datetime.today() - timedelta(hours = random.randint(1,5))
    context = {'user_list': user_list, 'plate': random_plate, 'time': random_time}
    body = "this is a twilio message for %s " % context['plate']
    mc.send_message(body, 7327151517)
    return render(request, 'streetparking/results.html', context, "")
    # return HttpResponse("results of the user")
