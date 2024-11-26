from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse("<h2>PAT CUMMINS IS THE CAPTAIN OF SRH</h1>")
def vicecaptain(request):
    return HttpResponse('<h1>NITISH KUMAR REDDY IS THE VICE CAPTAIN OF SRH</h1>')
def wicketkeeper(request):
    return HttpResponse('<h1>HEINRICH KLASSEN IS WICKET KEEPER FOR SRH</h1>')