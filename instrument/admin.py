from django.contrib import admin
from instrument.models import numOfYear, numOfMonth, numOfDay, numOfTime, numOfMonthAdmin, numOfDayAdmin, numOfTimeAdmin

admin.site.register(numOfYear)
admin.site.register(numOfMonth, numOfMonthAdmin)
admin.site.register(numOfDay, numOfDayAdmin)
admin.site.register(numOfTime, numOfTimeAdmin)
