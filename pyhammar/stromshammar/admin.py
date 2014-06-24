from django.contrib import admin

# Register your models here.
from .models import WallPost, NewsPost, GolfImage, GolfPost, FAQPost, GalleryImage, FiskeImage, FiskePost

class WallPostAdmin(admin.ModelAdmin):
    list_display = ('namn', 'timestamp', 'meddelande')

    class Meta:
        model = WallPost

class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'date', 'body_text')

    class Meta:
        model = NewsPost

class GolfImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'golf_post')

    class Meta:
        model = GolfImage

class GolfPostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date','body_text',)

    class Meta:
        model = GolfPost

class FiskeImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'fiske_post')

    class Meta:
        model = FiskeImage

class FiskePostAdmin(admin.ModelAdmin):
    list_display = ('headline', 'pub_date','body_text',)

    class Meta:
        model = FiskePost

class FAQPostAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')

    class Meta:
        model = FAQPost

class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', )

admin.site.register(WallPost,WallPostAdmin)
admin.site.register(NewsPost, NewsPostAdmin)
admin.site.register(GolfImage, GolfImageAdmin)
admin.site.register(GolfPost, GolfPostAdmin)
admin.site.register(FAQPost, FAQPostAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(FiskeImage, FiskeImageAdmin)
admin.site.register(FiskePost, FiskePostAdmin)