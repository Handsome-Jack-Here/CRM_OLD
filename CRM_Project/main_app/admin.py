from django.contrib import admin
from .models import Client, Order, Brand, Unit, Model, RepairStage, UnitType, Part, Services


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone_number', 'address', ]


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand', ]


@admin.register(Model)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['model', ]


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['brand', 'model', ]


@admin.register(RepairStage)
class RepairStageAdmin(admin.ModelAdmin):
    list_display = ['stage', ]


@admin.register(UnitType)
class UnitTypeAdmin(admin.ModelAdmin):
    list_display = ['unit_type', ]


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    list = '__all__'

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list = '__all__'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['pk', 'client', 'unit', 'defect', 'diagnostic_result', 'repair_stage']
    list_editable = ['repair_stage']
    list_display_links = ['pk', 'client', ]
