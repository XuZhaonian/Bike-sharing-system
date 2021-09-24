# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators import csrf
from django.test import TestCase
# from bikesharing.models import Testuser
from bikesharing.models import UserReg
from bikesharing import checkuser
import pandas as pd
import plotly.express as px

# Create your tests here.

def showplotly(request):
    return render(request, "templates/testmap.html")

# if __name__ == '__main__':
#     testplotly("../templates/testmap.html")

#

#
#
# def session_test(request):
#     request.session['h1'] = 'hello'
#     return HttpResponse('write session')
#
# def showmap(request):
#     return render(request, '../templates/homepage.html')

