from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def signup(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())