from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'morsemessenger/index.html')

def send(request):
    message = POST['message']
    return HttpResponseRedirect(reverse('morsemessenger:after',args=(message))

class after(request):
    return render(request,morsemessenger/postSend.html)
