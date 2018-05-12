from datetime import datetime
from django.utils import timezone

class Temperature(object):
     def __init__(self, temperature =0, max_temp = 0, min_temp = 0, record_day = None):
         self.temperature = temperature 
         self.max_temp = max_temp 
         self.min_temp = min_temp 
         if record_day is None:
            self.record_day = timezone.now
         else:
            self.record_day = record_day 

