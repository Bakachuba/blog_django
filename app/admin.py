from django.contrib import admin

from app.models import Creator, Post, Comment, Category, PostViewCount


@admin.register(Creator)
class CreatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user__username', 'created_at', 'post_count')
    search_fields = ('user__username',)
    ordering = ('-created_at',)

    def username(self, obj):
        return obj.user.username

    username.short_description = 'Имя пользователя'

    def post_count(self, obj):
        return obj.posts.count()

    post_count.short_description = 'Кол-во постов'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'creator', 'created_at', 'category_list')
    list_filter = ('created_at', 'categories')
    search_fields = ('title', 'content', 'creator__user__username')
    raw_id_fields = ('creator',)
    filter_horizontal = ('categories',)
    ordering = ('-created_at',)

    def category_list(self, obj):
        return ", ".join([cat.name for cat in obj.categories.all()])

    category_list.short_description = 'Категории'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_short', 'creator', 'post', 'created_at')
    search_fields = ('text', 'creator__user__username', 'post__title')
    list_filter = ('created_at',)

    def text_short(self, obj):
        return obj.text[:50]

    text_short.short_description = 'Комментарий'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(PostViewCount)
class PostViewCountAdmin(admin.ModelAdmin):
    list_display = ('posts', 'visitor', 'viewed_at')
    raw_id_fields = ('posts', 'visitor')
    ordering = ('-viewed_at',)
