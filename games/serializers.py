from rest_framework import serializers
from games.models import (
    Game,
    GameCategory,
    Player,
    PlayerScore
)

from games import views

class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedModelSerializer(
        many=True,
        read_only=True,
        view_name='game-detail'
    )

    class Meta:
        model = GameCategory
        fields = (
            'url',
            'pk',
            'name',
            'games'
        )

