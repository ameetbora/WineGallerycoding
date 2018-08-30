# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from chocofruitbox.models import Flower
from chocofruitbox.models import Chocolate

# Create your models here.
class Order(models.model)
    Order_ID
    CreatedAt
    UpdatedAt
    Paid
    User

    def get_order_total(self):

class OrderItemChocolate(models.model):
    order = models.ForeignKey(Order)
    chocolate = models.ForeignKey(Chocolate)
    price
    quantity


    def get_cost(self):
        # Calculate cost

class OrderItemFlower(models.model):
    order = models.ForeignKey(Order)
    flower = models.ForeignKey(Flower)
    price
    quantity

    def get_cost(self):
        ## Calculate cost
