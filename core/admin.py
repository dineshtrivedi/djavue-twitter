from django.contrib import admin

from core.models import ActivityLog, Todo, Payment, FuneralInsurance
from core.legacy_models import EmailAddresses


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class TodoAdmin(admin.ModelAdmin):
    list_display = ('description', 'done')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')

class FuneralInsuranceAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount')

class EmailAddressesAdmin(admin.ModelAdmin):
    list_display = ('index', 'name', 'email_address', 'phone_num')
    search_fields = ('phone_num', 'name')

admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(FuneralInsurance, FuneralInsuranceAdmin)
admin.site.register(EmailAddresses, EmailAddressesAdmin)
