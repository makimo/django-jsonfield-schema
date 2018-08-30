from django.core.exceptions import ValidationError
from jsonschema.exceptions import ValidationError as JSONSchemaValidationError


class JSONValidationError(ValidationError, JSONSchemaValidationError):
    def __init__(self, exc):
        super(JSONSchemaValidationError, self).__init__(
            exc.message,
            exc.validator,
            exc.path,
            exc.cause,
            exc.context,
            exc.validator_value,
            exc.instance,
            exc.schema,
            exc.schema_path,
            exc.parent
        )
