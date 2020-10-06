# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Function that shows the hello world with an Http Response.
    """
    return HttpResponse("Hello World, This is a Django App that has been deployed on Cloud Foundry 😄")

def warindex(request):
    return HttpResponse("Welcome to Wartown")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def pageSix(request):
    mando = 'westy'
    context = {'latest_question_list': mando}
    return render(request, 'index.html', context)

