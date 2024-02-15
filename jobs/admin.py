from django.contrib import admin
from .models import Job, Application


class JobAdmin(admin.ModelAdmin):
    list_display = ["title", "company", "location", "pub_date", "expiration_date"]
    search_fields = ["title", "company"]


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["job", "applicant_name", "applicant_email"]
    search_fields = ["job__title", "applicant_name", "applicant_email"]


admin.site.register(Job, JobAdmin)
admin.site.register(Application, ApplicationAdmin)
