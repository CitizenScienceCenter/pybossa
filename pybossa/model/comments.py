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

from sqlalchemy import Integer,Text
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.dialects.postgresql import TIMESTAMP
from pybossa.core import db
from pybossa.model import DomainObject, make_timestamp
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.ext.mutable import MutableDict, MutableList

class Comments(db.Model, DomainObject):
    '''A Counter lists the number of task runs for a given Task.'''

    __tablename__ = 'comments'

    #: Counter.ID
    id = Column(Integer, primary_key=True)
    #: UTC timestamp when the counter was created.
    created = Column(TIMESTAMP, default=make_timestamp)
    #: UTC timestamp when the counter was created.
    updated = Column(TIMESTAMP, default=make_timestamp)
    #: Project owner_id
    owner_id = Column(Integer, ForeignKey('user.id'))
    #: Project.ID that this counter is associated with.
    project_id = Column(Integer, ForeignKey('project.id'))
    #: parent ID
    parent = Column(Integer)
    #: content
    content = Column(MutableDict.as_mutable(JSONB), default=dict())
    #: text
    text = Column(Text)
    #: Project info field formatted as JSON
    info = Column(MutableDict.as_mutable(JSONB), default=dict())
