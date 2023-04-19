#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
"""Helper functions for executing GUI code in external scripts.

The intended use is for scripts such as cmk-update-config or init-redis.
"""

import typing
import warnings
from collections.abc import Iterator
from contextlib import contextmanager
from functools import lru_cache
from typing import Any

from flask import Flask
from flask.ctx import RequestContext
from werkzeug.test import create_environ

from cmk.gui.http import Response

Environments = typing.Literal["production", "testing", "development"]


@lru_cache
def session_wsgi_app(debug: bool = False, testing: bool = False) -> Flask:
    # TODO: Temporary hack. Can be removed once #12954 has been ported from 2.0.0
    from cmk.gui.wsgi.app import make_wsgi_app

    return make_wsgi_app(debug=debug, testing=testing)


def make_request_context(app: Flask, environ: dict[str, Any] | None = None) -> RequestContext:
    if environ is None:
        environ = create_environ()
    return app.request_context(environ)


@contextmanager
def request_context(app: Flask, environ: dict[str, Any] | None = None) -> Iterator[None]:
    with make_request_context(app, environ):
        app.preprocess_request()
        yield
        app.process_response(Response())


@contextmanager
def application_and_request_context(environ: dict[str, Any] | None = None) -> Iterator[None]:
    warnings.warn(
        "Please either use the `request_context` fixture or the `flask_app` fixture from now "
        "on. Using `flask_app` you can have access to the test client as well. "
        "See https://flask.palletsprojects.com/en/latest/testing/ and examples in our tests.",
        DeprecationWarning,
    )

    app = session_wsgi_app(testing=True)
    with app.app_context(), request_context(app, environ):
        yield


@contextmanager
def gui_context(environ: dict[str, Any] | None = None) -> Iterator[None]:
    app = session_wsgi_app(testing=True)
    with app.app_context(), make_request_context(app, environ):
        yield
