# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Global search data model for InvenioRDM."""

from flask import Flask

from . import config
from .resources import GlobalSearchRecordResource, GlobalSearchRecordResourceConfig
from .services import GlobalSearchRecordService, GlobalSearchRecordServiceConfig


class InvenioRecordsGlobalSearch:
    """Invenio-Records-Global-Search extension."""

    def __init__(self, app: Flask = None) -> None:
        """Construct InvenioRecordsGlobalSearch."""
        if app:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        """Flask application initialization."""
        self.init_config(app)
        self.init_services(app)
        self.init_resources()
        app.extensions["invenio-records-global-search"] = self

    def init_config(self, app: Flask) -> None:
        """Initialize configuration."""
        for k in dir(config):
            if k.startswith("GLOBAL_SEARCH_"):
                app.config.setdefault(k, getattr(config, k))

    def init_services(self, app: Flask) -> None:
        """Initialize services."""
        service_config = GlobalSearchRecordServiceConfig.build(app)
        self.records_service = GlobalSearchRecordService(config=service_config)

    def init_resources(self) -> None:
        """Initialize resources."""
        self.records_resource = GlobalSearchRecordResource(
            service=self.records_service,
            config=GlobalSearchRecordResourceConfig,
        )
