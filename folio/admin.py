from django.contrib import admin
from . models import *


# Register your models here.
class EducationAdmin(admin.ModelAdmin):
    list_display = ('format_date',)

    def format_date(self, obj):
        return obj.data.strftime('%b, %Y')

    format_date.admin_order_field = 'date'
    format_date.short_description = 'Date'
admin.site.register(Prot)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Client)
admin.site.register(Project)