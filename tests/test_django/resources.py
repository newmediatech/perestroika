from django.contrib.auth.models import User

from perestroika.methods import Get, Post, Put, Delete
from perestroika.resource import DjangoResource, JSONResource
from perestroika.validators import AllowAll


class EmptyDjangoResource(DjangoResource):
    pass


class EmptyJsonResource(JSONResource):
    pass


class OutUser:
    def __call__(self, item):
        return {"username": item["username"]}


class FullDjangoResource(DjangoResource):
    cache_control = dict(max_age=0, no_cache=True, no_store=True, must_revalidate=True)

    get = Get(
        queryset=User.objects.all(),
        output_validator=OutUser(),
        count_total=True
    )

    post = Post(
        queryset=User.objects.all(),
        input_validator=AllowAll(),
        output_validator=OutUser()
    )

    put = Put(
        queryset=User.objects.all(),
        input_validator=AllowAll(),
        output_validator=OutUser()
    )

    delete = Delete(
        queryset=User.objects.all()
    )


class FullJSONResource(JSONResource):
    cache_control = dict(max_age=0, no_cache=True, no_store=True, must_revalidate=True)

    get = Get(
        queryset=User.objects.all(),
        output_validator=OutUser(),
        count_total=True
    )

    post = Post(
        queryset=User.objects.all(),
        input_validator=AllowAll(),
        output_validator=OutUser()
    )

    put = Put(
        queryset=User.objects.all(),
        input_validator=AllowAll(),
        output_validator=OutUser()
    )

    delete = Delete(
        queryset=User.objects.all()
    )


__all__ = [
    "EmptyDjangoResource",
    "EmptyJsonResource",
    "FullDjangoResource",
    "FullJSONResource",
]
