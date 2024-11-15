from django.contrib import admin

# Register your models here.
from .models import Doctor,Designation,Specialization,AvailableTime,Review

class SpecializationAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug':('name',),}

class DesignationAdmin(admin.ModelAdmin):
     prepopulated_fields = {'slug':('name',),}
admin.site.register(Doctor)
admin.site.register(Review)
admin.site.register(Designation,DesignationAdmin)
admin.site.register(Specialization, SpecializationAdmin)
admin.site.register(AvailableTime)