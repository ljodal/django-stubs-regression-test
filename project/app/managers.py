from typing import TYPE_CHECKING, Optional

from django.db import models

if TYPE_CHECKING:
    from .models import MyModel


class MyManager(models.Manager):
    def my_manager_method(self) -> None:
        ...


class MyQuerySet(models.QuerySet["MyModel"]):
    def my_method(self, arg: int) -> Optional["MyModel"]:
        return self.first()
