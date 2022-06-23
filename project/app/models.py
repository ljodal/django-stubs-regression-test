from django.db import models

from .managers import MyManager, MyQuerySet

_MyManager = MyManager.from_queryset(MyQuerySet)


class MyModel(models.Model):

    objects = _MyManager()
