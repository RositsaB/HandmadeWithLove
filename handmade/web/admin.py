from django.contrib import admin

from handmade.web.models import Project, Favourites, Comment, News


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Favourites)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass
