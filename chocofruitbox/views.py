# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request):
    ## If User logged in and Subscribed
    ## Can view their recommended Chocolates
    ## Add Flowers from Catalogue
    ## If not logged in or not subscribed
    ## User can look at the different Chocolate and Flower catalogue
    ## Render HTML response