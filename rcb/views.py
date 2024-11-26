from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def captain(request):
    return HttpResponse("<h2>KING KOHLI IS THE CAPTAIN OF RCB</h1>")
def vicecaptain(request):
    return HttpResponse('<h1>BHUVI IS THE VICE CAPTAIN OF RCB</h1>')
def wicketkeeper(request):
    return HttpResponse('<h1>DINESH KARTHIK IS WICKET KEEPER FOR RCB</h1>')