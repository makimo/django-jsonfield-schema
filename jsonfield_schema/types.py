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
        return name, path, args, kwargs

    def validate(self, value, model_instance):
        try:
            validate(value, self.schema)
            super().validate(value, model_instance)
        except JSONSchemaValidationError as e:
            raise JSONValidationError(e)

    def contribute_to_class(self, cls, name, private_only=False):
        def validate_field(self):
            try:
                schema = self._meta.get_field(name).schema
                validate(getattr(self, name), schema)
            except JSONSchemaValidationError as e:
                raise JSONValidationError(e)

        setattr(cls, 'validate_{}'.format(name), validate_field)
        super().contribute_to_class(cls, name, private_only=False)
