# -*- coding: utf-8 -*-

# MIT License

# Copyright (c) 2018-2020 Renondedju

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN TH
# SOFTWARE.

from sqlalchemy     import Column, Integer, Text
from sqlalchemy.orm import relationship

from isartbot.database import TableBase

class Server(TableBase):

    __tablename__ = 'servers'

    id                   = Column('id'               , Integer, primary_key = True, unique = True)
    lang                 = Column('lang'             , Text   , default     = "en")
    discord_id           = Column('discord_id'       , Integer, unique      = True)
    modlog_channel_id    = Column('modlog_channel_id', Integer, default     = 0)
    live_role_id         = Column('live_role_id'     , Integer, default     = 0)
    starboard_channel_id = Column('starboard_id'     , Integer, default     = 0)
    starboard_minimum    = Column('starboard_minimum', Integer, default     = 3)
    verified_role_id     = Column('verified_role_id' , Integer, default     = 0)
    
    games                 = relationship('Game'              , cascade='all,delete,delete-orphan')
    self_assignable_roles = relationship('SelfAssignableRole', cascade='all,delete,delete-orphan')
