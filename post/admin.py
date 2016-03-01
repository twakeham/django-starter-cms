from django.contrib.admin import ModelAdmin, site

from models import Post, Category


class PostAdmin(ModelAdmin):
    list_display = ['title', 'slug', 'created', 'published']
    prepopulated_fields = {"slug": ("title",)}
site.register(Post, PostAdmin)


class CategoryAdmin(ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    
site.register(Category, CategoryAdmin)