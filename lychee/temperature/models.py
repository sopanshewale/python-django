from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from datetime import datetime 

class Temperature(models.Model):
       temperature = models.PositiveIntegerField(
                     verbose_name=_('Current Temperatuer in Cel'),
                     default = 0,
       )
       min_temp = models.PositiveIntegerField(
                     verbose_name=_('Current Temperatuer in Cel'),
                     default = 0,
       )
       max_temp = models.PositiveIntegerField(
                     verbose_name=_('Current Temperatuer in Cel'),
                     default = 0,
       )
       entry_time = models.DateTimeField(
                    default= timezone.now,
                    verbose_name=_('Entry Time'),
                    blank=True, null=True,
      )
  
  
  

