# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from django.urls import path

from .views import DataView
from .views import SignUpView
from .views import SignInView


urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('signin/<int:player_id>/', SignInView.as_view()),
    path('data/<int:player_id>/', DataView.as_view()),
]
