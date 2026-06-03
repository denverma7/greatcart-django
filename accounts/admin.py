from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.
# override user admin to show the fields that we want to show in admin panel
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'first_name', 'last_name') # to make the email, first name and last name as clickable link in admin panel
    read_only_fields = ('last_login', 'date_joined') # to make the last login and date joined fields as read only fields in admin panel
    ordering = ('-date_joined',) # to order the users by date joined in descending order in admin panel

    # to make the email field as read only field in admin panel
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
