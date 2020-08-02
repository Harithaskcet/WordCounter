
from django.http import HttpResponse
from django.shortcuts import render
import operator

def homePage(request):
    return HttpResponse('Congo!!you have reached the word counter homepage')

def search(request):
    key = request.GET.get('keyword')
    response = "you have searched for the keyword "+key+" in the application"
    return HttpResponse(response)

def home(request):
    return render(request, 'Home.js',{'hi':'hello'})

def about(request):
    return HttpResponse("<h1>Welcome!! this is about the word counter application</h1>")

def count(request):
    inputs = request.GET.get('inputBox')
    length = inputs.split()
    dictionary = {}
    for x in length:
        if x in dictionary:
            counts = dictionary.get(x)
            dictionary[x] = counts+1
        else:
            dictionary[x] = 1
    dictionary = sorted(dictionary.items(),key=operator.itemgetter(1), reverse = True)
    return render(request, 'Count.html',{'char':inputs, 'count': len(length), 'words':dictionary})
