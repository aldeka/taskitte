from kittehs.models import List, Task, Person, TinyMailingList
from django.contrib import admin

class TaskInline(admin.StackedInline):
    model = Task
    extra = 3
    
class ListAdmin(admin.ModelAdmin):
    inlines = [TaskInline]

admin.site.register(List, ListAdmin)

admin.site.register(Person)