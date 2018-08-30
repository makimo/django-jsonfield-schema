import pytest

from jsonfield_schema import TypedJSONField, JSONValidationError

from .models import Foo


@pytest.mark.django_db
def test_validation_plain_obj():
    obj = Foo.objects.create(json={})

    with pytest.raises(JSONValidationError):
        obj.field = 1
        obj.save()
