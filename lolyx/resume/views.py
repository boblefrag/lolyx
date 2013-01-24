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
"""
The resume views
"""
import logging

from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from lolyx.resume.models import Resume
from lolyx.resume.forms import ResumeForm


logger = logging.getLogger(__name__)


class ResumeView(DetailView):

    model = Resume

    def get_context_data(self, **kwargs):
        context = super(ResumeView, self).get_context_data(**kwargs)
        context['now'] = "toto"
        return context


class ResumeEdit(DetailView):

    model = Resume

    def get_context_data(self, **kwargs):
        context = super(ResumeEdit, self).get_context_data(**kwargs)
        return context

    def get(self, *args, **kwargs):
        # Security to edit only own resume
        self.object = self.get_object()
        if self.request.user.id != self.object.user.id:
            return redirect('/accounts/profile')
        #return http.HttpResponsePermanentRedirect('/accounts/profile/')
        return super(CanonicalDetailView, self).get(*args, **kwargs);


def new(request):
    """
    The home page
    """
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            Resume.objects.create(title=form.cleaned_data['title'],
                                  user=request.user)
            return redirect('/accounts/profile/')
    else:
        form = ResumeForm()


    return render(request,
                  'resume/new.html',
                  {'form': form})
