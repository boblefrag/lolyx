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
Models definition for caro app
"""
import logging
from django.db import models


class Company(models.Model):
    """
    The company object

    """
    name = models.CharField(max_length=300,
                            verbose_name='Name')


class Job(models.Model):
    """
    The job object

    """
    company = models.ForeignKey(Company)
    title = models.CharField(max_length=300,
                             verbose_name='Job title',
                             blank=True)

    status = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        """
        The unicode method
        """
        return self.title

    def activate(self):
        """
        The job is activate and published online
        """
        logger = logging.getLogger(__name__)
        logger.debug('activate job %s' % self.id)

        self.status = 1
        self.save()


class Tool(models.Model):
    """
    The tools known by candidat or required by companies

    """
    name = models.CharField(max_length=30,
                            verbose_name='Tool name')

    url = models.URLField(max_length=300)

    category = models.IntegerField(default=0)

    oldid = models.IntegerField(default=0)

    # identi.ca category name
    identi = models.CharField(max_length=30,
                              blank=True)


class Contract(models.Model):
    """
    The tools known by candidat or required by companies

    """
    code = models.CharField(max_length=30,
                            verbose_name='Contract name')

    def __unicode__(self):
        """
        The unicode method
        """
        return self.code

    def __str__(self):
        """
        The unicode method
        """
        return self.code


class Website(models.Model):
    """
    The tools known by candidat or required by companies

    """
    name = models.CharField(max_length=30,
                            verbose_name='Tool name')

    url = models.URLField(max_length=300)
    userpage = models.URLField(max_length=300)
