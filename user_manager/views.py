from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from user_manager.froms import LoginForm
from django.contrib.auth import authenticate, login


class LoginView(View):

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            print("request.user ->", request.user)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if(user):
                login(request, user)
                print(request.user)
            return HttpResponseRedirect('/msg/view/')
        else:
            return render(request, 'login.html', {'form':form})    

    def get(self, request):
        form = LoginForm()
        
        return render(request, 'login.html', {'form':form})
