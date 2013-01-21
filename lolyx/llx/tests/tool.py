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
Unit tests for Tool

"""
from django.test import TestCase
from lolyx.llx.models import Tool


class ToolTests(TestCase):  # pylint: disable-msg=R0904
    """
    The main tests
    """

    def test_create(self):
        """
        Create a simple tool
        """
        tool = Tool.objects.create(name='git')

        self.assertTrue(tool.id > 0)
