# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def create_order(request):
    ## Calls forms from forms.py
    ## Call the celery task to create the order and save it
    ## render html response