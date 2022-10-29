from django.contrib import admin

from alarms.models import Alarm, AlarmHistory

# Register your models here.
admin.site.register(Alarm)
admin.site.register(AlarmHistory)