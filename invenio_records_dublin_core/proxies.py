# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Helper proxy to the state object."""

from flask import current_app
from werkzeug.local import LocalProxy

current_records_dublin_core = LocalProxy(
    lambda: current_app.extensions["invenio-records-dublin-core"],
)
"""Helper proxy to get the dublin core extension."""
