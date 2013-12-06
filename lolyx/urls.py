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
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^accounts/', include('registration.urls')),
                       url(r'^cv/', include('lolyx.resume.urls')),
                       url(r'^offres/', include('lolyx.resume.urls')),
                       url(r'^accounts/profile/$', 'lolyx.llx.views.profile'),
                       url(r'^$', 'lolyx.llx.views.home', name='home'),
                       url(r'^search/cv/$', RedirectView.as_view(url=reverse_lazy('resume'))),
                       # TODO: Use reverse_lazy and not hard the path
                       url(r'^search/cv/date.php$', RedirectView.as_view(url='/cv/date/')),

)
