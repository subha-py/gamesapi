from rest_framework import serializers
from games.models import (
    Game,
    GameCategory,
    Player,
    PlayerScore
)

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
    game_category =serializers.SlugRelatedField(
        queryset=GameCategory.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Game
        fields = (
            'url',
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



# http POST :8000/games/ name='Tetris Reloaded' game_category='2D mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'
# http POST :8000/games/ name='Puzzle Craft' game_category='2D mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'
# http POST :8000/games/ name='Blek' game_category='2D mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'
# http POST :8000/games/ name='Scribblenauts Unlimited' game_category='2D mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'
# http POST :8000/games/ name='Cut the Rope: Magic' game_category='2D mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'
# http POST :8000/games/ name='Tiny Dice Dungeon' game_category='2D mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'
# http POST :8000/games/ name='A Dark Room' game_category='2D mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'
# http POST :8000/games/ name='Bastion' game_category='2D mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'
# http POST :8000/games/ name='Welcome to the Dungeon' game_category='2D mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'
# http POST :8000/games/ name='Dust: An Elysian Tail' game_category='2D mobile arcade' played=false release_date='2016-06-21T03:02:00.776594Z'