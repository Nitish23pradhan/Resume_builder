from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('resume_id', 'name', 'email', 'short_content', 'downloads')
    search_fields = ('name', 'email')
    readonly_fields = ('resume_id',)

    def short_content(self, obj):
        return obj.content[:50] + "..."