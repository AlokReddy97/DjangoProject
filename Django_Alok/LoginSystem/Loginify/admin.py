from django.contrib import admin
from .models import UserDetails

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')  # Fields to display in the list view
    search_fields = ('username', 'email')  # Add a search bar for these fields
    list_filter = ('email',)  # Add filters based on the email field

admin.site.register(UserDetails, UserDetailsAdmin)