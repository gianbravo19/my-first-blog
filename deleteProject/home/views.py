# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse


# Templates

indexTemplate = 'home/index.html'


# Views


# Index view

def index(request):

	# Answer
	
	return render(request, indexTemplate, {})
    
