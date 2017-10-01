from django.contrib.auth.models import User
from django_filters import (
    NumberFilter,
    DateTimeFilter,
    AllValuesFilter
)

from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import permissions
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import filters

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    ListAPIView,
    RetrieveAPIView
)

from games.models import (
    GameCategory,
    Game,
    Player,
    PlayerScore
)

from games.serializers import (
    GameCategorySerializer,
    GameSerializer,
    PlayerSerializer,
    PlayerScoreSerializer,
)

from games.serializers import UserSerializer
from games.permissions import IsOwnerOrReadOnly




class ApiRoot(GenericAPIView):
    name= 'api-root'

    def get(self,request,*args,**kwargs):
        return Response(
            {
                'players':reverse(PlayerList.name,request=request),
                'game-categories':reverse(GameCategoryList.name,request=request),
                'game':reverse(GameList.name,request=request),
                'scores':reverse(PlayerScoreList.name,request=request),
                'users': reverse(UserList.name,request=request)
            }
        )




class GameCategoryList(ListCreateAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-list'
    throttle_scope = 'game-categories'
    throttle_classes = (ScopedRateThrottle,)
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)

class GameCategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = GameCategory.objects.all()
    serializer_class = GameCategorySerializer
    name = 'gamecategory-detail'
    throttle_scope = 'game-categories'
    throttle_classes = (ScopedRateThrottle,)

class GameList(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )
    filter_fields = (
        'name',
        'game_category',
        'release_date',
        'played',
        'owner',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
        'release_date',
    )

    def perform_create(self, serializer):
        # pass an additional owner field to the create method
        # to set the owner to the user recieved in the request
        serializer.save(owner=self.request.user)

class GameDetail(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    name = 'game-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    )

class PlayerList(ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-list'
    filter_fields = (
        'name',
        'gender',
    )
    search_fields = (
        '^name',
    )
    ordering_fields = (
        'name',
    )

class PlayerDetail(RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    name = 'player-detail'


class PlayerScoreFilter(filters.FilterSet):
    min_score = NumberFilter(
        name='score',lookup_expr='gte'
    )
    max_score = NumberFilter(
        name='score',lookup_expr='lte'
    )
    from_score_date = DateTimeFilter(
        name='score_date',
        lookup_expr='gte'
    )
    to_score_date = DateTimeFilter(
        name='score_date',
        lookup_expr='lte'
    )
    player_name = AllValuesFilter(
        name='player__name'
    )
    game_name = AllValuesFilter(
        name= 'game__name'
    )

    class Meta:
        model = PlayerScore
        fields = (
            'score',
            'from_score_date',
            'to_score_date',
            'min_score',
            'max_score',
            # player__name will be accessed as player_name
            'player_name',
            #game__name will be accessed as game_name
            'game_name'
        )



class PlayerScoreList(ListCreateAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-list'
    filter_class =PlayerScoreFilter
    ordering_fields = (
        'score',
        'score_date',
    )


class PlayerScoreDetail(RetrieveUpdateDestroyAPIView):
    queryset = PlayerScore.objects.all()
    serializer_class = PlayerScoreSerializer
    name = 'playerscore-detail'

class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'

class UserDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'