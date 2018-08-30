# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.model):
    user = models.OneToOneField(User)
    picture = models.ImageField()
    Subscription = models.ForeignKey(OnetoOne)

class Subscription(models.model):
    Subscription_ID
    Subscription_Name
    Subcription_Type
    CreatedAt
    UpdatedAt

class Chocolate(models.model):
    Choc_ID
    Choc_Name
    Choc_Price
    Choc_Type
    Available
    CreatedAt
    UpdatedAt
    image

class Flower(models.model):
    Flower_ID
    name
    price
    type
    available
    image
    created
    updated