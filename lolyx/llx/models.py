# -*- coding: utf-8 -*-
#
# Copyright (c) 2012 Rodolphe Quiédeville <rodolphe@quiedeville.org>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
Models definition for caro app
"""
import logging
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from datetime import timedelta


class Job(models.Model):
    """
    The job object

    """
    title = models.CharField(max_length=300,
                             verbose_name='Job title',
                             blank=True)

    status = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        """
        The unicode method
        """
        return self.title

    def activate(self):
        """
        A user like this song
        """
        logger = logging.getLogger(__name__)
        logger.debug('activate job %s' % self.id)

        self.status = 1
        self.save()
