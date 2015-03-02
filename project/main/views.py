from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def events(request):
    return render(request, 'events.html')

def contact(request):
    return render(request, 'contact.html')

def resources(request):
    return render(request, 'resources.html')