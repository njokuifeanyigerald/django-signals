from django.contrib import admin
from .models import Signal

class SignalAdmin(admin.ModelAdmin):
    model = Signal
    list_display = ['name', 'age','complexion', 'job',]
    search_fields = ['name','age', 'job',]
    list_filter = ['complexion']
    fields = [
        'name', 'age','complexion', 'job',
    ]

admin.site.register(Signal, SignalAdmin)
