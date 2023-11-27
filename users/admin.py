from django.contrib import admin
from .models import User, HistoryModel


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["username", "first_name", "last_name", "card_id"]


admin.site.register(User, AuthorAdmin)
admin.site.register(HistoryModel)

