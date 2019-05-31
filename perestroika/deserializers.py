import json

from perestroika.exceptions import BadRequest
from perestroika.utils import multi_dict_to_dict


class Deserializer:
    def deserialize(self, request, method_handler, **kwargs):
        raise NotImplementedError()


class DjangoDeserializer(Deserializer):
    def deserialize(self, request, method_handler, **kwargs):
        if request.method == 'GET':
            _data = multi_dict_to_dict(request.GET)
        else:
            _data = json.loads(request.body)

        _items = _data.get("items", [])
        _item = _data.get("item")

        if _item:
            _items = [_item]

        if not _items and request.method in ["POST", "PUT", "PATCH"]:
            raise BadRequest(message="Need data for processing")

        bundle = {
            "order": _data.get("order"),
            "filter": _data.get("filter"),
            "items": _items,
            "limit": 20,
            "skip": 0,
            "total_count": 0,
            "queryset": method_handler.queryset,
            "project": _data.get("project", []),
        }

        return bundle


class JsonDeserializer(Deserializer):
    def deserialize(self, request, handler, **kwargs):
        ws_data = kwargs.get("ws_data", {})
        method = kwargs.get("method", {})

        _items = ws_data.get("items", [])
        _item = ws_data.get("item")

        if _item:
            _items = [_item]

        if not _items and method in ["post", "put", "patch"]:
            raise BadRequest(message="Need data for processing")

        bundle = {
            "order": ws_data.get("order"),
            "filter": ws_data.get("filter"),
            "items": _items,
            "limit": 20,
            "skip": 0,
            "total_count": 0,
            "queryset": handler.queryset,
            "project": ws_data.get("project", []),
            "meta": ws_data.get("meta", {}),
        }

        return bundle
