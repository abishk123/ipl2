from django.shortcuts import render

from django.http import HttpResponse

def captain(request):
    return HttpResponse("<h2>RUTHURAJ GAIKWAD IS THE CAPTAIN OF CSK</h1>")
def vicecaptain(request):
    return HttpResponse('<h1>SIR JADEJA IS THE VICE CAPTAIN OF CSK</h1>')
def wicketkeeper(request):
    return HttpResponse('<h1>MS.DHONI IS WICKET KEEPER FOR CSK</h1>')

