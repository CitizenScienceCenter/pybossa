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

from sqlalchemy.exc import IntegrityError
from sqlalchemy import cast, Date

from pybossa.repositories import Repository
from pybossa.model.comments import Comments
from pybossa.model.user import User
from pybossa.core import uploader
from pybossa.exc import WrongObjectError, DBIntegrityError

class CommentRepository(Repository):

    def __init__(self, db):
        self.db = db

    def get(self, id):
        return self.db.session.query(Comments).get(id)

    def get_by_parent_id(self, id):
        return self.db.session.query(Comments).filter_by(parent=id).order_by(Comments.id.desc())

    def get_threads_user(self, id):
        users = self.db.session.query(User).get(1)
        threads = self.db.session.query(Comments).filter_by(parent=id).order_by(Comments.id.desc())
        return threads.join(users, threads.owner_id==users.id)


    def count_comments_with_parent_id(self, id):
        return self.db.session.query(Comments).filter_by(parent=id).count()

    def get_by(self, **attributes):
        return self.db.session.query(Comments).filter_by(**attributes).first()

    def filter_by(self, limit=None, offset=0, yielded=False, last_id=None,fulltextsearch=None, desc=True,
                  **filters):
        return self._filter_by(Comments, limit, offset, yielded,last_id, fulltextsearch,desc, **filters)

    def save(self, comment):
        #self._validate_can_be('saved', comment)
        try:
            self.db.session.add(comment)
            self.db.session.commit()
            #clean_project(comment.project_id)
        except IntegrityError as e:
            self.db.session.rollback()
            raise DBIntegrityError(e)

    def update(self, comment):
        #self._validate_can_be('updated', comment)
        try:
            self.db.session.merge(comment)
            self.db.session.commit()
            #clean_project(blogpost.project_id)
        except IntegrityError as e:
            self.db.session.rollback()
            raise DBIntegrityError(e)

    def delete(self, comment):
        #self._validate_can_be('deleted', comment)
        comment = self.db.session.query(Comments).filter(Comments.id==comment.id).first()
        self.db.session.delete(comment)
        self.db.session.commit()
        #clean_project(project_id)

    def delete_topic_replies(self,com):
        comment = self.db.session.query(Comments).filter(Comments.parent==com.id).delete()
        #self.db.session.delete(comment)
        self.db.session.commit()
        #clean_project(project_id)
