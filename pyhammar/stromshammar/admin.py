from django.contrib import admin

# Register your models here.
from .models import WallPost, NewsPost

class WallPostAdmin(admin.ModelAdmin):
    class Meta:
        model = WallPost

class NewsPostAdmin(admin.ModelAdmin):
    class Meta:
        model = NewsPost

admin.site.register(WallPost,WallPostAdmin)
admin.site.register(NewsPost, NewsPostAdmin)