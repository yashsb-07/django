from django.contrib import admin
from .models import GameVarity, GameReview, Store, GameCertificate

# Register your models here.
class GameReviewInline(admin.TabularInline):
    model = GameReview
    extra = 2

class GameVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    inlines = [GameReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('game_varieties',)

class GameCertificateAdmin(admin.ModelAdmin):
    list_display = ('game', 'certificate_number')




admin.site.register(GameVarity, GameVarietyAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(GameCertificate, GameCertificateAdmin)
