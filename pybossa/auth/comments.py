# -*- coding: utf8 -*-
# This file is part of PYBOSSA.
#
# Copyright (C) 2015 Scifabric LTD.
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


class CommentsAuth(object):
    _specific_actions = []

    def __init__(self, project_repo):
        self.project_repo = project_repo

    @property
    def specific_actions(self):
        return self._specific_actions

    def can(self, user, action, comment=None, project_id=None):
        action = ''.join(['_', action])
        return getattr(self, action)(user, comment, project_id)

    def _update(self, user, comment, project_id=None):
        if user.is_anonymous:
            return False
        return comment.owner_id == user.id or user.admin

    def _delete(self, user, comment, project_id=None):
        if user.is_anonymous:
            return False
        return comment.owner_id == user.id or user.admin

    def _get_project(self, blogpost, project_id):
        if blogpost is not None:
            return self.project_repo.get(blogpost.project_id)
        return self.project_repo.get(project_id)

    def _is_admin_or_owner(self, user, project):
        return (not user.is_anonymous and
                (user.admin or user.id in project.owners_ids))
