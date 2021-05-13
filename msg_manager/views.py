from django.http.response import HttpResponse
from django.shortcuts import render


def send_message(request):
    if('message' in request.POST):
        print(request.POST)
        name = request.POST['name']
        return render(request, 'response.html', {'name':name})
    else:
        return render(request, 'home.html')
