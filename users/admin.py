from django.contrib import admin

from users.models import Profile

# Register your models here.
#admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #Profile admin

    #Change the order on how it's shown
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')

    #Define what values re clickable
    list_display_links = ('pk', 'user')

    #What values can be easily editable
    list_editable = ('phone_number', 'website', 'picture')

    #Where to search
    search_fields = (
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    #Django filters
    list_filter = (
        'created',
        'modified',
        'user__is_active',
        'user__is_staff'
    )
