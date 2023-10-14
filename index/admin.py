from django.contrib import admin

from index.models import Event, Category
@admin.register(Category)
class PersonAdmin(admin.ModelAdmin):
    pass
@admin.register(Event)
class PersonAdmin(admin.ModelAdmin):
    pass