from django.contrib import admin
from .models import DCPUlogin,Organization,Branches,Children,Attendence,Problem,Funds,Problemsolution,Donations,Fundusagebills

admin.site.register(DCPUlogin)
admin.site.register(Organization)
admin.site.register(Branches)
admin.site.register(Children)
admin.site.register(Attendence)
admin.site.register(Problem)
admin.site.register(Funds)
admin.site.register(Problemsolution)
admin.site.register(Donations)
admin.site.register(Fundusagebills)
# Register your models here.
