from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse("<h2>ROHITH SHARMA IS THE CAPTAIN OF MI</h1>")
def vicecaptain(request):
    return HttpResponse('<h1>HARDIK PANDYA IS THE VICE CAPTAIN OF MI</h1>')
def wicketkeeper(request):
    return HttpResponse('<h1>TILAK VARMA IS WICKET KEEPER FOR MI</h1>')
