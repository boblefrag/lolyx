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
Test all public and private urls
"""
from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client
from lolyx.resume.models import Resume


class UrlsTests(TestCase):  # pylint: disable-msg=R0904
    """
    The urls
    """
    def setUp(self):
        """
        set up the tests
        """
        Resume.objects.all().delete()
        self.user = User.objects.create_user('foobar',
                                             'admin_search@bar.com',
                                             'admintest')

    def test_view(self):
        """
        The view
        """
        resume = Resume.objects.create(title='Senior admin',
                                       user=self.user)

        client = Client()
        response = client.get('/cv/{}/'.format(resume.id))

        self.assertContains(response, resume.title, status_code=200)

    def test_new_resume(self):
        """
        The view
        """
        client = Client()
        response = client.get('/cv/new/')

        self.assertContains(response, 'form', status_code=200)

    def test_edit(self):
        """
        The view
        """
        resume = Resume.objects.create(title='Senior admin',
                                       user=self.user)

        client = Client()
        client.login(username='foobar', password='admintest')
        response = client.get('/cv/edit/{}/'.format(resume.id))

        self.assertContains(response, resume.title, status_code=200)

