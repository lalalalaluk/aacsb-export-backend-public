from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as _UserAdmin

# Register your models here.
from django.contrib.auth.forms import UserCreationForm
from django.forms import forms

from app.user.models import User


class UserCreationForm(UserCreationForm):
    """
    A UserCreationForm with optional password inputs.
    """

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].required = False
        self.fields['password2'].required = False
        # If one field gets autocompleted but not the other, our 'neither
        # password or both password' validation will be triggered.
        self.fields['password1'].widget.attrs['autocomplete'] = 'off'
        self.fields['password2'].widget.attrs['autocomplete'] = 'off'

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = super(UserCreationForm, self).clean_password2()
        if bool(password1) ^ bool(password2):
            raise forms.ValidationError("Fill out both fields")
        return password2


class UserAdmin(_UserAdmin):
    list_display = ['username', 'email', 'unit', 'contact', 'date_joined', 'is_superuser', 'is_staff',
                    'is_active']
    search_fields = ['email', 'username', 'date_joined']

    fieldsets = (
        ('基本資料', {'fields': ('email', 'username', 'unit', 'contact', 'password')}),
        ('權限管理', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        ('登入狀態', {'fields': ('date_joined', 'last_login')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'unit', 'contact', 'password1', 'password2'),
        }),
    )
    add_form = UserCreationForm


admin.site.register(User, UserAdmin)
