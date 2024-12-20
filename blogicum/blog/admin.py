from django.contrib import admin  # type: ignore[import-untyped] # noqa: F401
from .models import Category, Location, Post

# Register your models here.
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Post)