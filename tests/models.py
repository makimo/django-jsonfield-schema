from django.db import models

from jsonfield_schema import TypedJSONField


class Foo(models.Model):
    json = TypedJSONField(schema={
        "type" : "object",
        "properties" : {
            "price" : {"type" : "number"},
            "name" : {"type" : "string"}
        }
    })
