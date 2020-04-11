from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import New_user
from posts.models import Post


class PostsInLine(admin.StackedInline):
    model = Post
    extra = 1


class ViewUserAdmin(admin.ModelAdmin):
    fields = ['name', 'photo', 'status']
    inlines = [PostsInLine]

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()



admin.site.register(New_user, AccountAdmin)
