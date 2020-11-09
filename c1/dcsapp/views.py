from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    template = loader.get_template('default.html')
    context = { 'page': 'null' }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def delta(request):
    template = loader.get_template('polls/home.html')
    context = { 'myname': 'boba' }
    return HttpResponse(template.render(context, request))

def home(request):
    template = loader.get_template('polls/home.html')
    context = { 'page': 'null' }
    return HttpResponse(template.render(context, request))

def compute(request):
    template = loader.get_template('polls/compute.html')
    context = { 'page': 'null' }
    return HttpResponse(template.render(context, request))

def storage(request):
    template = loader.get_template('polls/storage.html')
    context = { 'page': 'null' }
    return HttpResponse(template.render(context, request))

def data(request):
    template = loader.get_template('polls/data.html')
    context = { 'page': 'null' }
    return HttpResponse(template.render(context, request))

def info(request):
    template = loader.get_template('polls/info.html')
    context = { 'page': 'null' }
    return HttpResponse(template.render(context, request))