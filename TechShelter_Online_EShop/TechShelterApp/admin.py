from django.contrib import admin

from .models import User, Tech, OrderInfo, OrderedTech
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model=User
    add_form=CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets, (
            'More Information', {
                'fields': (
                    'image',
                    'location',
                    'usertype'
                )
            }
        )
    )

admin.site.register(User, CustomUserAdmin)

admin.site.register(Tech)

admin.site.register(OrderInfo)

admin.site.register(OrderedTech)