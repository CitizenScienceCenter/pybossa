# -*- coding: utf8 -*-
# This file is part of PYBOSSA.
#
# Copyright (C) 2017 Scifabric LTD.
#
# PYBOSSA is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PYBOSSA is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PYBOSSA.  If not, see <http://www.gnu.org/licenses/>.
"""
PYBOSSA api module for domain object Announcement via an API.

This package adds GET, POST, PUT and DELETE methods for:
    * announcement

"""
from api_base import APIBase
from pybossa.model.announcement import Announcement
from pybossa.core import user_repo, project_repo
from flask.ext.login import current_user
from werkzeug.exceptions import BadRequest, NotFound

from flasgger.utils import swag_from

class AnnouncementAPI(APIBase):

    """Class API for domain object Announcement."""

    reserved_keys = set(['id', 'created', 'updated', 'user_id'])

    __class__ = Announcement

    @swag_from('swagger/announcement/GET.yml')
    def get(self, oid):
        return APIBase.get(self, oid)

    @swag_from('swagger/announcement/PUT.yml')
    def put(self, oid):
        return APIBase.put(self, oid)

    @swag_from('swagger/announcement/POST.yml')
    def post(self):
        return APIBase.post(self)

    @swag_from('swagger/announcement/DELETE.yml')
    def delete(self, oid):
        return APIBase.put(self, oid)

    def _forbidden_attributes(self, data):
        for key in data.keys():
            if key in self.reserved_keys:
                raise BadRequest("Reserved keys in payload")

    def _update_object(self, obj):
        if not current_user.is_anonymous():
            obj.user_id = current_user.id
