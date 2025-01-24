from django.contrib import admin

# Register your models here.
from .models import Post, Feedback, PostCategory

admin.site.register(Post)
admin.site.register(Feedback)
admin.site.register(PostCategory)