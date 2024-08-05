from django.contrib import admin
from app_resume.models import Resume, WorkExperience

class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'job_title', 'about', 'field_type')
    list_editable = ('job_title', )
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'job_title')

admin.site.register(Resume, ResumeAdmin)

class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'resume')
    list_filter = ('resume', )

admin.site.register(WorkExperience, WorkExperienceAdmin)