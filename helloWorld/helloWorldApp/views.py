from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    output = "{\"Message\": \"Hello World!\"}"
    template = loader.get_template('helloWorldApp/index.html')
    context = {'output': output}
    return HttpResponse(template.render(context, request))
