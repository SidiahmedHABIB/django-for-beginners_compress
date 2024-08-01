from django.contrib import admin
from .models import Post, Blog, CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('date_joined', 'last_login')
    
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Personal', {'fields': ('first_name', 'last_name')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )

admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(CustomUser, CustomUserAdmin)
