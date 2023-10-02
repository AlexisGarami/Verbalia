from django.contrib import admin
from .models import Task, Calificacion, Plan, Group, Performance, StudentEntry, Attendance, AttendanceEntry

class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )
    
class PlanAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date','user', 'group', )


class StudentEntryInline(admin.TabularInline):
    model = StudentEntry
    extra = 0

class PerformanceAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date', 'user', 'group', )
    inlines = [StudentEntryInline]

class AttendanceEntryInline(admin.TabularInline):
    model = AttendanceEntry
    extra = 0

class AttendanceAdmin(admin.ModelAdmin):
    readonly_fields = ('creation_date', 'user', 'group', )
    inlines = [AttendanceEntryInline]

# Register your models here.

admin.site.register(Task, TaskAdmin)
admin.site.register(Calificacion)
admin.site.register(Plan, PlanAdmin)
admin.site.register(Group)
admin.site.register(Performance, PerformanceAdmin)
admin.site.register(Attendance, AttendanceAdmin)