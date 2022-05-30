from django.contrib import admin
from web.models import Portfolio, Employer, Message, SendToEmail, Blog
# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Blog)
admin.site.register(Employer)
admin.site.register(SendToEmail)
admin.site.register(Message)