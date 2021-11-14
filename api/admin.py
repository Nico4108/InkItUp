from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Tattooparlor

# Register your models here.

admin.site.register(Tattooparlor, UserAdmin)
'''
class UserAdmin(BaseUserAdmin):

  form = UserChangeForm
  fieldsets = (
      (None, {'fields': ('name', 'password', )}),
      (_('Personal info'), {'fields': ('email', 'phonenumber')}),
      (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
      (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('user_info'), {'fields': ('supplier_cvr', 'adress', 'cvr')}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide', ),
          'fields': ('email', 'password1', 'password2'),
      }),
  )
  list_display = ['email', 'name', 'is_staff', "cvr", "phonenumber"]
  search_fields = ('email', 'name', 'phonenumber')
  ordering = ('email', )
  '''
