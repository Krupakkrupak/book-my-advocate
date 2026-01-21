from django.contrib import admin
from .models import Advocate, Case

@admin.register(Advocate)
class AdvocateAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'experience_years', 'hourly_rate', 'availability', 'created_at')
    list_filter = ('specialization', 'availability', 'created_at')
    search_fields = ('user__first_name', 'user__last_name', 'specialization')
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'advocate', 'status', 'case_type', 'created_at', 'closed_at')
    list_filter = ('status', 'case_type', 'created_at', 'advocate')
    search_fields = ('title', 'client__first_name', 'client__last_name', 'advocate__user__first_name')
    readonly_fields = ('created_at', 'updated_at', 'closed_at')
