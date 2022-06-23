from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from .managers import UserQuerySet

UserManager = models.Manager.from_queryset(UserQuerySet)


class User(AbstractBaseUser):

    email = models.EmailField(unique=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
