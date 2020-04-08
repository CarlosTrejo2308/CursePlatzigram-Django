from django.contrib import admin

from users.models import Profile

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import User

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

    # How to show a user
    # Category - Data
    #Its managed by tuples
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            ),
        }),
        ('Metadata', {
                'fields': (('created', 'modified'),)
            }),
    )

    #This fields cannot be modified
    readonly_fields = ('created', 'modified', 'user')

#Creates the section to add
class ProfileInLine(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

#Add user admin to base user admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInLine,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)

#Modelo - Clase
#Adds more to create a user
admin.site.register(User, UserAdmin)
