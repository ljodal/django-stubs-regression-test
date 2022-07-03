from typing import TypeVar

from django.db import models

T = TypeVar("T", bound=models.Model)


class MyQuerySet(models.QuerySet[T]):
    pass


class MyManager(models.Manager[T]):
    pass


class SecondManager(models.Manager[T]):
    pass
