# ☭ perestroika

[![Build Status](https://travis-ci.org/newmediatech/perestroika.svg?branch=master)](https://travis-ci.org/newmediatech/perestroika) 
[![Coverage Status](https://coveralls.io/repos/github/newmediatech/perestroika/badge.svg?branch=master)](https://coveralls.io/github/newmediatech/perestroika)
[![PyPI version](https://badge.fury.io/py/perestroika.svg)](https://badge.fury.io/py/perestroika)

- [About](#about)
- [Installation](#installation)
- [Usage](#usage)

### <a name="about"/>About</a>
Simple REST framework for django

### <a name="installation"/>Installation</a>
With pip:
```bash
pip install perestroika
```

### <a name="usage"/>Usage</a>
```python
from django.contrib.auth.models import User
from perestroika.resource import DjangoResource
from perestroika.methods import Get, Post
from perestroika.exceptions import RestException



class Validator:
    def __call__(self, item: dict) -> dict:
        return {'username': item['username']}


def reject_not_superuser(request, bundle):
    if not request.user.is_superuser:
        raise RestException(message="Unauthorized", status_code=401)

    
def add_is_superuser_flag(request, bundle):
    for user in bundle['items']:
        user['is_superuser'] = True


class SuperUserResource(DjangoResource):
    # use django @cache_control kwargs
    cache_control = dict(max_age=0, no_cache=True, no_store=True, must_revalidate=True)

    # allowed method GET
    get = Get(
        # base queryset
        queryset=User.objects.filter(is_superuser=True),
        
        # restrict access
        request_hooks = [
            reject_not_superuser
        ],
        
        # any callable
        output_validator=Validator,
    )
    
    # allowed method POST
    post = Post(
        # restrict access
        request_hooks = [
            reject_not_superuser
        ],
    
        # process incoming data
        pre_query_hooks=[
            add_is_superuser_flag
        ],

        # any callable
        input_validator=Validator,
    )
```
