from django.contrib.auth.models import Group, Permission
from django.db import models
from typing_extensions import reveal_type

from .managers import MyManager, MyQuerySet, SecondManager

FirstManager = MyManager.from_queryset(MyQuerySet)


class FirstModel(models.Model):
    objects = FirstManager()


def test_1() -> None:
    reveal_type(FirstModel.objects)
    reveal_type(FirstModel.objects.first)
    reveal_type(FirstModel.objects.filter)
    reveal_type(FirstModel.objects.all().filter)


class SecondModel(models.Model):
    objects = SecondManager.from_queryset(MyQuerySet)()


def test_2() -> None:
    reveal_type(SecondModel.objects)
    reveal_type(SecondModel.objects.first)
    reveal_type(SecondModel.objects.filter)
    reveal_type(SecondModel.objects.all().filter)
    reveal_type(SecondModel._default_manager)


class CustomManager(models.Manager):
    def custom_method(self):
        pass


class ThirdModel(models.Model):
    objects = CustomManager()


class FourthModel(models.Model):
    objects = CustomManager()


def test_3() -> None:
    reveal_type(ThirdModel.objects)
    reveal_type(ThirdModel.objects.all)
    reveal_type(ThirdModel.objects.all())
    reveal_type(ThirdModel.objects.filter)
    reveal_type(ThirdModel.objects.custom_method)

    reveal_type(FourthModel.objects.custom_method)
