from django.contrib import admin

from app.models import Building


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'floor_number', 'unit', 'created_time', 'parking', 'patio', 'lobby',
                    'automatic_door', 'emergency_system', 'Fire_alarm_system', 'Powerhouse', 'cooler', 'fire_capsules',
                    'lighting_detail', 'trashcans', 'Wastewater', 'elevator']
    list_filter = ['created_time']
