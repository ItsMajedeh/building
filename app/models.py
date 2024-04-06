from django.db import models
from django.utils.translation import gettext_lazy as _


class Building(models.Model):
    name = models.CharField(verbose_name=_('اسم'), max_length=50)
    floor_number = models.PositiveIntegerField(verbose_name=_('تعداد طبقات'))
    unit = models.PositiveIntegerField(verbose_name=_('تعداد واحد'))
    created_time = models.DateTimeField(verbose_name=_('سال ساخت'))
    parking = models.BooleanField(verbose_name=_('پارکینگ'), default=True)
    patio = models.BooleanField(verbose_name=_('حیاط'), default=True)
    lobby = models.BooleanField(verbose_name=_('لابی'), default=True)
    automatic_door = models.BooleanField(verbose_name=_('درب ریموت دار'), default=True)
    emergency_system = models.BooleanField(verbose_name=_('سیستم برق اظطراری'), default=True)
    Fire_alarm_system = models.BooleanField(verbose_name=_('سیستم اعلام حریق'), default=True)
    Powerhouse = models.BooleanField(verbose_name=_('موتورخانه'), default=True)
    cooler = models.BooleanField(verbose_name=_('کولر'), default=True)
    fire_capsules = models.BooleanField(verbose_name=_('کپسول آتش نشانی'), default=True)
    lighting_detail = models.TextField(verbose_name=_('سیستم روشنایی'))
    trashcans = models.PositiveIntegerField(verbose_name=_('سطل زباله'))
    Wastewater = models.BooleanField(verbose_name=_('فاضلاب'), default=True)
    elevator = models.BooleanField(verbose_name=_('آسانسور'), default=True)

    def __str__(self):
        return f'{self.name}'


class Services(models.Model):
    POWERHOUSE = 1
    ELEVATOR = 2
    COOLER = 3

    SERVICE_TYPE_CHOICES = (
        (POWERHOUSE, _("موتورخانه")),
        (ELEVATOR, _("آسانسور")),
        (COOLER, _("کولر")),
    )
    building = models.ForeignKey(to=Building, verbose_name=_('ساختمان'), related_name='building',
                                 on_delete=models.PROTECT)
    service_type = models.PositiveSmallIntegerField(_('نوع سرویس'), choices=SERVICE_TYPE_CHOICES)
    service_time = models.DateTimeField(_('زمان سرویس'))

    def __str__(self):
        return f'{self.building}, {self.service_type}'
