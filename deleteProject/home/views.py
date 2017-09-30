# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse


# Views


def index(request):


    return HttpResponse("Hi GIAN !! You get it !! ")
    
