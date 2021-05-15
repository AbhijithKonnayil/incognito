from django.http.response import HttpResponse
from django.shortcuts import render
from msg_manager.models import Message


def send_message(request):
    if('message' in request.POST):
        name = request.POST['name']
        msg = request.POST['message']
        Message.objects.create(msg=msg)
        return render(request, 'response.html', {'name':name})
    else:
        return render(request, 'home.html')
