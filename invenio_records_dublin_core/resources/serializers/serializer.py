# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-dublin-core is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Invenio Dublin Core Record Resource serializers."""


from flask_resources import BaseListSchema, JSONSerializer
from flask_resources.serializers import MarshmallowSerializer

from .schema import DublinCoreSchema


class DublinCoreJSONSerializer(MarshmallowSerializer):
    """Dublin Core base serializer implementation."""

    def __init__(self) -> None:
        """Dublin Core Base Serializer Constructor.

        :param schema_cls: Default DublinCoreSchema
        :param options: Json encoding options.
        """
        super().__init__(
            format_serializer_cls=JSONSerializer,
            object_schema_cls=DublinCoreSchema,
            list_schema_cls=BaseListSchema,
        )
