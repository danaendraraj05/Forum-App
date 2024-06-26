from django.contrib import admin
from .models import Board, Topic, Post

class BoardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'board', 'starter', 'last_updated')
    search_fields = ('subject', 'starter__username', 'board__name')
    list_filter = ('board', 'starter', 'last_updated')
    ordering = ('-last_updated',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('message_excerpt', 'topic', 'created_at', 'created_by', 'updated_at', 'updated_by')
    search_fields = ('message', 'created_by__username', 'topic__subject')
    list_filter = ('created_at', 'updated_at', 'created_by', 'updated_by')
    ordering = ('-created_at',)

    def message_excerpt(self, obj):
        return obj.message[:30]
    message_excerpt.short_description = 'Message Excerpt'

admin.site.register(Board, BoardAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Post, PostAdmin)
