from django.contrib import admin

# Register your models here.
from .models import Category,Movie,Genre,RatingStar,Rating,MovieShots,Actor,Reviews


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "url", "name")
    list_display_links = ("name",)
    

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title","category","url","draft")
    list_filter = ("category","year")
    search_fields = ("title","category__name")






admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Reviews)
