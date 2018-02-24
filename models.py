# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Document(models.Model):
    docfile = models.ImageField(upload_to='documents/%Y/%m/%d')
