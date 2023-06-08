from django.contrib import admin
from post.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'created_date', 'updated_date', 'status')
admin.site.register(Post, PostAdmin)