from django.urls import path

from tests.test_django.resources import EmptyDjangoResource, EmptyJsonResource, \
    FullDjangoResource, FullJSONResource

urlpatterns = [
    path('empty_django/', EmptyDjangoResource().handler),
    path('empty_json/', EmptyJsonResource().handler),
    path('full_django/', FullDjangoResource().handler),
    path('full_json/', FullJSONResource().handler),
]
