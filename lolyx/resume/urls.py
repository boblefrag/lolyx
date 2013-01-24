# -*- coding: utf-8 -*-  pylint: disable-msg=R0801
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
from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
from django.contrib.auth.decorators import login_required
from lolyx.resume.views import ResumeView
from lolyx.resume.views import ResumeEdit

urlpatterns = patterns('',
                       url(r'^(?P<pk>\d+)/$', ResumeView.as_view()),
                       url(r'^edit/(?P<pk>\d+)/$', login_required(ResumeEdit.as_view())),
                       url(r'^new/$', 'lolyx.resume.views.new'),
                       url(r'^$', 'lolyx.llx.views.home', name='resume')
)
