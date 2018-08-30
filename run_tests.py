#!/usr/bin/env python
import os
import sys

import pytest

import django
from django.conf import settings

if __name__ == "__main__":
    os.environ['DJANGO_SETTINGS_MODULE'] = 'test_settings'
    django.setup()

    sys.exit(bool(pytest.main(['tests/test_validation.py'])))
