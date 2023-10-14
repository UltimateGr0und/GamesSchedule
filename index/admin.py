from django.contrib import admin

from index.models import Person, Course, Grade
@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass