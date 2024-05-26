from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from account.models import User,user_otp,Address,Contact,Profile
from .forms import UserCreationForm,UserChangeForm







class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ["Phone","email", "is_admin"]
    list_filter = ["is_admin"]
    fieldsets = [
        (None, {"fields": ["Phone", "password"]}),
        ("اطلاعات شخصی", {"fields": ["Fullname"]}),
        ("دسترسی ها", {"fields": ["is_admin"]}),
        ("ایمیل",{"fields":["email"]})
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["Phone","Fullname","password1", "password2"],
            },
        ),
    ]
    search_fields = ["Phone"]
    ordering = ["Phone"]
    filter_horizontal = []
@admin.register(Contact)
class Contactadmin(admin.ModelAdmin):
    list_display = ("name","subject")

admin.site.register(Address)
admin.site.register(Profile)
# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)
admin.site.register(user_otp)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)
