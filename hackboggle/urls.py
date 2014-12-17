from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'game.views.index', name='home'),
    #url(r'^game/', include('game.urls', namespace='game')),
    url(r'^game/new_board/', 'game.views.new_board'),
    url(r'^admin/', include(admin.site.urls)),
)
