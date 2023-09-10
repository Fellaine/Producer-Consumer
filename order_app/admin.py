from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Employee, Order

# Register your models here.


class MyUserAdmin(UserAdmin):
    model = Employee

    fieldsets = UserAdmin.fieldsets + (
        (
            None,
            {
                "fields": (
                    "probation",
                    "position",
                )
            },
        ),
    )


admin.site.register(Order)
admin.site.register(Employee, MyUserAdmin)
