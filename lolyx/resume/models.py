# -*- coding: utf-8 -*-
#
# Copyright (c) 2013 Rodolphe Quiédeville <rodolphe@quiedeville.org>
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
Models definition for resume
"""
from django.db import models
from django.contrib.auth.models import User
from lolyx.llx.models import Website


class Resume(models.Model):
    """
    The company object

    """
    title = models.CharField(max_length=300,
                             verbose_name='Title')

    status = models.IntegerField(default=0)

    user = models.ForeignKey(User)

    email = models.EmailField(max_length=300)
    email_verified = models.BooleanField(default=False)

    date_published = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class PeopleRessource(models.Model):

    resume = models.ForeignKey(Resume)
    website = models.ForeignKey(Website)

    login = models.CharField(max_length=300)
