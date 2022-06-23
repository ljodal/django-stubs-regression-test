from typing import TYPE_CHECKING, Optional

from django.db import models

if TYPE_CHECKING:
    from .models import User


class UserQuerySet(models.QuerySet["User"]):
    pass
