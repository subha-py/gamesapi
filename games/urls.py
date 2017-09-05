from django.conf.urls import url
from games import views

urlpatterns = [
    url(r'^$',views.game_list),
    url(r'^(?P<pk>[0-9]+)/$',views.game_detail),
]