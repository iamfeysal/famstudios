from django.contrib import admin
from .models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created", "slug", "image", "publish", "status")
    list_filter = ("title", "created", "image", "publish", "status")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = "publish"
    ordering = ["status", "publish"]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
