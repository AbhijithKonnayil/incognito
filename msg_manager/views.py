from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from msg_manager.models import Message
from django.views import View


class SendMessage(View):

    def get(self, request):
        return render(request, 'home.html')
    
    def post(self, request):
        name = request.POST['name']
        msg = request.POST['message']
        obj = Message.objects.create(msg=msg)
        print(obj.msg)
        return render(request, 'response.html', {'name':name})


def view_msg(request):
    if(request.method == 'GET'):
        msgs = Message.objects.all()
        return render(request, 'view_msgs.html', {'msgs':msgs, 'temp':'Temp Msg'})
         
