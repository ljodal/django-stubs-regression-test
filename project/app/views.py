from django.http import HttpRequest
from typing_extensions import reveal_type

HttpRequest().user


def view(request: HttpRequest) -> None:
    reveal_type(request.user)
