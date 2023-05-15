from django.db import models
from django.contrib.auth.models import User

class Good_or_Bad(models.Model):
    reason = models.CharField(max_length = 180)
    is_good_day = models.BooleanField(default = False, blank = True)
    timestamp = models.DateTimeField(auto_now = True, blank = True)

    def __str__(self):
        return "Good day" if self.is_good_day else "Bad Day"