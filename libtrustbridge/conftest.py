import pytest
from flask import Flask

from libtrustbridge.errors import handlers


class TestConfig():
    DEBUG = True
    TESTING = True


@pytest.yield_fixture()
def app():
    app = Flask('common_api_errors_test_app')
    app.config.from_object(TestConfig)
    handlers.register(app)
    yield app
