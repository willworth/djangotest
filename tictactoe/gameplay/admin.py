from django.contrib import admin

from .models import Game, Move


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_player', 'second_player', 'status')
    list_editable = ('status',)
    #comma above is to indicate it's a tuple


admin.site.register(Move)