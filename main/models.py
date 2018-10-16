from django.db import models

# Create your models here.
class Zones(models.Model):
    timezone = models.CharField(max_length=50, blank=True, null=True)
    sat = models.CharField(max_length=100, blank=True, null=True)
    sun = models.CharField(max_length=100, blank=True, null=True)
    others = models.CharField(max_length=100, blank=True, null=True)

class Schedule(models.Model):
    track = models.CharField(max_length=50, blank=False, null=True, verbose_name='Track')
    grade = models.CharField(max_length=20, blank=False, null=True, verbose_name='Grade')
    timezone = models.CharField(max_length=50, blank=False, null=True, verbose_name='Timezone')
    slotaday = models.CharField(max_length=50, blank=False, null=True, verbose_name='SlotA day')
    slota = models.CharField(max_length=50, blank=False, null=True, verbose_name='SlotA Time')
    slotbday = models.CharField(max_length=50, blank=True, null=True, verbose_name='SlotB day')
    slotb = models.CharField(max_length=50, blank=True, null=True, verbose_name='SlotB Time')
    stuname = models.CharField(max_length=255, blank=True, null=True, verbose_name='Student Name')
    pemail = models.EmailField(blank=False, null=True, verbose_name='Parent Email')
    phone = models.CharField(max_length=255, blank=True, null=True, verbose_name='Phone Number')
    created = models.DateTimeField(null=True, blank=False, auto_now_add=True, verbose_name='Created At')
    pstslota = models.CharField(max_length=50, blank=False, null=True, verbose_name='Time in PST SlotA')
    istslota = models.CharField(max_length=50, blank=False, null=True, verbose_name='Time in IST SlotA')
    pstslotb = models.CharField(max_length=50, blank=False, null=True, verbose_name='Time in PST SlotB')
    istslotb = models.CharField(max_length=50, blank=False, null=True, verbose_name='Time in IST SlotB')
    contact = models.BooleanField(null=False, blank=True, default=False, verbose_name='Contact')
    
    def __str__(self):
        return self.stuname
