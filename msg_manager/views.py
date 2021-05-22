from msg_manager.forms import MsgForm
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render
from msg_manager.models import Message
from django.views import View
from django.contrib.auth.models import User


class SendMessage(View):

    def get(self, request, username):
        form = MsgForm()
        print(username)
        return render(request, 'home.html', {'form':form})
    
    def post(self, request, username):
        msg = request.POST['msg']
        user = User.objects.get(username=username)
        obj = Message.objects.create(msg=msg, user=user)
        print(obj.msg)
        return render(request, 'response.html',)


def view_msg(request):
    if(request.method == 'GET'):
        msgs = Message.objects.filter(user=request.user)
        return render(request, 'view_msgs.html', {'msgs':msgs, 'temp':'Temp Msg'})
         
