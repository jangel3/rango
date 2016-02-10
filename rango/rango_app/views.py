from django.http import HttpResponse
from django.shortcuts import render


context_dict = {'boldmessage': "I am bold font from the context"}

def index(request):
    return render(request, 'rango/index.html', context_dict)


def about(request):
    return HttpResponse("Rango Says: Here is the about page.<br/><a href='/rango/'>Home</a>")