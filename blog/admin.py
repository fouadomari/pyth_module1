from django.contrib import admin
from .models import User, Post, Comment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'is_active', 'created_at')
    search_fields = ('name', 'phone_number')
    list_filter = ('is_active', 'created_at')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_id', 'title', 'user', 'date')
    search_fields = ('title', 'content', 'user__name')
    list_filter = ('date', 'user')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'short_text', 'created_at')
    search_fields = ('text', 'user__name', 'post__title')
    list_filter = ('created_at', 'user', 'post')

    def short_text(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text
    short_text.short_description = 'Comment Text'