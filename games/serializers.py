from rest_framework import serializers
from games.models import (
    Game,
    GameCategory,
    Player,
    PlayerScore
)

from django.contrib.auth.models import User

class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
    games = serializers.HyperlinkedRelatedField(
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

class GameSerializer(serializers.HyperlinkedModelSerializer):
    # we just want to display the owner username (read - only)
    owner = serializers.ReadOnlyField(source='owner.username')
    # We want to display the game category's name instead of the id
    game_category =serializers.SlugRelatedField(
        queryset=GameCategory.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Game
        fields = (
            'url',
            'owner',
            'game_category',
            'name',
            'release_date',
            'played'
        )


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    game = GameSerializer()

    class Meta:
        model = PlayerScore
        fields = [
            'url',
            'pk',
            'score',
            'score_date',
            'game',
        ]

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    scores = ScoreSerializer(many=True,read_only=True)
    gender = serializers.ChoiceField(
        choices = Player.GENDER_CHOICE
    )
    gender_description = serializers.CharField(
        source='get_gender_display',
        read_only=True
    )

    class Meta:
        model = Player
        fields = [
            'url',
            'name',
            'gender',
            'gender_description',
            'scores',
        ]

class PlayerScoreSerializer(serializers.ModelSerializer):
    player = serializers.SlugRelatedField(queryset=Player.objects.all(),
                                          slug_field='name')
    game=serializers.SlugRelatedField(queryset=Game.objects.all(),slug_field='name')

    class Meta:
        model = PlayerScore
        fields = [
            'url',
            'pk',
            'score',
            'score_date',
            'player',
            'game'
        ]

class UserGameSerialzer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = (
            'url',
            'name'
        )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    games = UserGameSerialzer(many=True,read_only=True)

    class Meta:
        model = User
        fields = [
            'url',
            'pk',
            'username',
            'games'
        ]