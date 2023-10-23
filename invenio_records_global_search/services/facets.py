# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 Graz University of Technology.
#
# invenio-records-global-search is free software; you can redistribute it and/or
# modify it under the terms of the MIT License; see LICENSE file for more
# details.

"""Facets."""

from invenio_i18n import gettext as _
from invenio_records_resources.services.records.facets import TermsFacet

data_model = TermsFacet(
    field="original.schema",
    label=_("DataModel"),
)

subjects = TermsFacet(
    field="metadata.subjects",
    label=_("Subjects"),
)

publishers = TermsFacet(
    field="metadata.publishers",
    label=_("Publishers"),
)

formats = TermsFacet(
    field="metadata.formats",
    label=_("Formats"),
)

rights = TermsFacet(
    field="metadata.rights",
    label=_("Rights"),
    value_labels={
        "https://creativecommons.org/licenses/by/4.0": _("CC BY 4.0"),
        "https://creativecommons.org/licenses/by-sa/4.0": _("CC BY-SA 4.0"),
        "https://creativecommons.org/licenses/by-nd/4.0": _("CC BY-ND 4.0"),
        "https://creativecommons.org/licenses/by-nc/4.0": _("CC BY-NC 4.0"),
        "https://creativecommons.org/licenses/by-nc-sa/4.0": _("CC BY-NC-SA 4.0"),
        "https://creativecommons.org/licenses/by-nc-nd/4.0": _("CC BY-NC-ND 4.0"),
    },
)

types = TermsFacet(
    field="metadata.types",
    label=_("Types"),
)
