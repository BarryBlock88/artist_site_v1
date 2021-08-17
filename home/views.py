from django.shortcuts import render

# Create your views here.

def index(request):
    """ a view """
    return render(request, 'home/index.html')