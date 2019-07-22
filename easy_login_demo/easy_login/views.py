# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.contrib.auth import login
from django.views.generic.base import View
from django.conf import settings
from django.urls import reverse

from .forms import SwitchUserForm


class EasyLoginView(View):
    form_class = SwitchUserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            if user is not None:
                login(request, user)

        if hasattr(settings, 'EASY_URL_REDIRECT'):
            url = reverse(settings.EASY_URL_REDIRECT)

            return HttpResponseRedirect(url)

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
