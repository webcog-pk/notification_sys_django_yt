from django.contrib import admin
from notification.models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ['user','message','is_read', 'timestamp']

admin.site.register(Notification, NotificationAdmin)
# Register your models here.
