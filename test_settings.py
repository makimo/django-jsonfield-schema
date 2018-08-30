#!/usr/bin/env python
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'fake-key'

SITE_ID = 1

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'jsonfield_schema',
    'tests'
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'host': 'localhost',
        'PORT': '5432',
        'TEST': {
            'CHARSET': 'UTF8',
            'NAME': 'json_test'
        }
    }
}
