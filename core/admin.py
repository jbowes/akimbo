from core.models import Story, Sprint, Task
from django.contrib import admin

class TaskAdmin(admin.ModelAdmin):
    list_display = ['name', 'assigned', 'remaining', 'estimate']
    list_filter = ['assigned']
    search_fields = ['title']

admin.site.register(Story)
admin.site.register(Sprint)
admin.site.register(Task, TaskAdmin)
