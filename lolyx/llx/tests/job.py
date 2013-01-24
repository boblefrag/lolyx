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
Unit tests for Job object

"""
from django.contrib.auth.models import User
from django.test import TestCase
from lolyx.llx.models import Job
from lolyx.llx.models import Company


class JobTests(TestCase):  # pylint: disable-msg=R0904
    """
    The main tests
    """
    def setUp(self):
        """
        set up the tests
        """
        self.user = User.objects.create_user('foobar',
                                             'admin_search@bar.com',
                                             'admintest')

    def test_create(self):
        """
        Create a simple job
        """
        company = Company.objects.create(name='Lolix')
        job = Job.objects.create(title='Senior admin',
                                 company=company)

        self.assertTrue(job.id > 0)
