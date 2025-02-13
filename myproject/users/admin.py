from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Comments, Category

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"title_slug": ("title", )}
 
admin.site.register(User, UserAdmin)
admin.site.register(Comments)
admin.site.register(Category, CategoryAdmin)

