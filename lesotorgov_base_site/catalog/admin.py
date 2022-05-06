from django.contrib import admin
from .models import Type, Variety, Lumber, LumberInstance, StampCement, Cement, CementInstance, StampMetal, Metal, \
    MetalInstance

# Register your models here.
admin.site.register(Type)
admin.site.register(Variety)
admin.site.register(Lumber)
admin.site.register(StampCement)
admin.site.register(Cement)
admin.site.register(StampMetal)
admin.site.register(Metal)


@admin.register(LumberInstance)
class LumberInstanceAdmin(admin.ModelAdmin):
    list_display = ('lumber', 'count', 'type')
    list_filter = ('status', 'due_back')


@admin.register(CementInstance)
class CementInstanceAdmin(admin.ModelAdmin):
    list_display = ('cement', 'count')
    list_filter = ('status', 'due_back')


@admin.register(MetalInstance)
class MetalInstanceAdmin(admin.ModelAdmin):
    list_display = ('metal', 'count')
    list_filter = ('status', 'due_back')
