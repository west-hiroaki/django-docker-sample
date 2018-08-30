# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from datetime import datetime

from django.db import models


class Player(models.Model):
    # 名前
    _name = models.CharField(max_length=128)
    # 最終ログイン日時
    last_login_at = models.DateTimeField()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError('name is required.')

        self._name = name

    @classmethod
    def get_by(cls, player_id):
        return cls.objects.filter(pk=player_id).first()

    @classmethod
    def create(cls, name):
        """
        プレイヤー生成処理.
        :param string name: プレイヤー名
        """
        player = Player()

        player.name = name
        player.last_login_at = datetime.now()
        player.save()

        return player

    @classmethod
    def login(cls, player_id):
        """
        ログイン処理.
        最終ログイン日時を更新する.
        :param int player_id: 対象プレイヤーID
        """
        cls.objects.filter(pk=player_id). \
            update(last_login_at=datetime.now())
