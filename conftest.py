from __future__ import unicode_literals

import os

import pytest
from django.core.cache import cache

from django_project import settings

pytestmark = pytest.mark.django_db(transaction=True)


@pytest.fixture(scope="session", autouse=True)
def clean_cache():
    cache.clear()


def pytest_configure():
    try:
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
    except OSError as e:
        raise Exception("Unknown exception creating media dir")


def is_integration(request) -> bool:
    try:
        for mark in request.keywords._markers["pytestmark"]:
            if "integration" in mark.name:
                return True
    except:
        return False
    return False


def pytest_addoption(parser):
    group = parser.getgroup('selenium', 'selenium')
    group._addoption('--headless',
                     action='store_true',
                     help='enable headless mode for supported browsers.')


@pytest.fixture
def chrome_options(chrome_options, pytestconfig):
    if os.path.isfile('/usr/bin/chromium'):
        chrome_options.binary_location = '/usr/bin/chromium'
    elif os.path.isfile('/usr/bin/google-chrome-unstable'):
        chrome_options.binary_location = '/usr/bin/google-chrome-stable'
    else:
        chrome_options.binary_location = '/usr/bin/google-chrome-unstable'
    if pytestconfig.getoption('headless'):
        chrome_options.add_argument('--headless')
    return chrome_options


@pytest.fixture
def firefox_options(firefox_options, pytestconfig):
    firefox_options.binary = '/usr/bin/firefox'

    if pytestconfig.getoption('headless'):
        firefox_options.add_argument('-headless')
    return firefox_options
