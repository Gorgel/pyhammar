from django.contrib import admin

# Register your models here.
from .models import WallPost

class WallPostAdmin(admin.ModelAdmin):
    class Meta:
        model = WallPost

admin.site.register(WallPost,WallPostAdmin)