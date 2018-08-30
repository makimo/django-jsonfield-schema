from django.contrib.postgres.fields.jsonb import JSONField
from jsonschema import validate
from jsonschema.exceptions import ValidationError as JSONSchemaValidationError

from .exceptions import JSONValidationError


class TypedJSONField(JSONField):
    schema = None
    def __init__(self, schema=None, *args, **kwargs):
        self.schema = schema
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        # del kwargs['schema']
        return name, path, args, kwargs

    def __get__(self, instance, owner):
        return self._value

    def __set__(self, instance, value):
        self.validate(value, instance)
        self._value = value

    def validate(self, value, model_instance):
        try:
            validate(value, self.schema)
            super().validate(value, model_instance)
        except JSONSchemaValidationError as e:
            raise JSONValidationError(e)
