from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Category, Messages, Equipment, Comments, Journal
from django.utils.safestring import mark_safe   


admin.site.site_header = 'Панель администрирования'

class UserAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'third_name',
                        'job', 'department', 'username', 'password', 'email',
                        ]
    fields = ['first_name', 'last_name', 'third_name',
                    'job', 'department', 'username', 'password', 'email',]
    search_fields = ['job', 'first_name', 'last_name', 'email', 'username']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    fields = ['title', 'slug']
    prepopulated_fields = {"slug": ("title", )}
    search_fields = ['title', 'slug']


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['body', 'owner', 'sender', 'time_create']
    search_fields = ['body']


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['title', 'place', 'cat', 'characteristic', 'slug', 'get_html_photo']
    prepopulated_fields = {"slug": ("title", )}
    search_fields = ['title', 'slug']

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")
        else:
            return "Нет фото"
        
    get_html_photo.short_description = "Фото"


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'equipment', 'time_create']
    search_fields = ['user', 'equipment']


class JournalAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'body', 'user', 'time_create']
    search_fields = ['user', 'equipment']


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Messages, MessagesAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Journal, JournalAdmin)