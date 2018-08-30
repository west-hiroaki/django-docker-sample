# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.db import transaction
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Player


class SignUpView(TemplateView):
    template_name = 'sign_up.html'

    def get(self, request, *args, **kwargs):
        name = request.GET.get('name', None)

        player = Player.create(name)

        context = {
            'player': player,
        }
        return render(self.request, self.template_name, context)


class SignInView(TemplateView):
    template_name = 'data.html'

    def get(self, request, *args, **kwargs):
        player_id = kwargs['player_id']

        Player.login(player_id)

        context = {
            'player': Player.get_by(player_id),
        }
        return render(self.request, self.template_name, context)


@transaction.non_atomic_requests
class DataView(TemplateView):
    template_name = 'data.html'

    def get(self, request, *args, **kwargs):
        player_id = kwargs['player_id']

        context = {
            'player': Player.get_by(player_id),
        }
        return render(self.request, self.template_name, context)
