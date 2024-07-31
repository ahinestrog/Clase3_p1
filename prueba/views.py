from django.shortcuts import render
from django.http import HttpResponse

from .models import Prueba

# Create your views here.
def home(request):
    #return HttpResponse('<h1>Welcome home page</h1>')
    #return render(request,'home.html')
    #return render(request,'home.html',{'name':'Alejandro Hinestroza'})
    searchTerm = request.GET.get('searchMovie')
    if searchTerm:
        movies = Prueba.objects.filter(title__icontains=searchTerm)
    else:
        movies = Prueba.objects.all()
    return render(request,'home.html',{'searchTerm':searchTerm,'movies':movies})


def about(request):
    #return HttpResponse('<h1>About page</h1>')
    return render(request,'about.html')
