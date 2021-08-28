from django.shortcuts import render
#from django.views import View

def home(request):
    context={}
    return render(request, 'home.html',context)


