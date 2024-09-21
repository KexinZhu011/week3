from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def members(request):
    return render(request, 'register.html')

# def members(request):
#   template = loader.get_template('register.html')
#   return HttpResponse(template.render())