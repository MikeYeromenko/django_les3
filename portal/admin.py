from django.contrib import admin

from portal import models


# Register your models here.
class CommentsInline(admin.TabularInline):
    model = models.Comment
    # readonly_fields = ['user', 'text']
    extra = 0


class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'title', 'is_deleted', 'author']
    # list_editable = ['title']
    list_display_links = ['title']
    raw_id_fields = ['author']

    inlines = [
        CommentsInline
    ]


admin.site.register(models.PortalUser)
admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Comment)
admin.site.register(models.Like)
admin.site.register(models.Source)
admin.site.register(models.Tag)
