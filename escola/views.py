from django.shortcuts import render


# Create your views here.

def index(request):

    context = {
        'welcome' : 'Welcome to KemSoftware',
        'begin' : 'Starting my first page By Kemuel Kesley'
    }

    return render(request, 'index.html', context)



def contato(request):
    return render(request, 'contato.html')   