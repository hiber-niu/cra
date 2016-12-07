#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import View


class HomeView(View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)

    # def populate_other_context(self, request, context):
        # pass
