import datetime
from django.db import models
from django.urls import reverse

class Call(models.Model):
    timestampstart = models.DateTimeField(verbose_name='Start')
    timestampend = models.DateTimeField(verbose_name='End',null=True,blank=True)
    source = models.CharField(verbose_name='Source',max_length=9)
    destination = models.CharField(verbose_name='Destination',max_length=9)
    def get_absolute_url(self):
        return reverse('call_edit', kwargs={'pk': self.pk})
    def get_seconds(self):
        s = int((self.timestampend-self.timestampstart).total_seconds())
        return s
    seconds = property(get_seconds)
    def duration(self):
        s = self.seconds
        h = s // 3600
        d = h // 86400
        r = s % 3600
        m = r // 60
        r = r % 60
        if (h >= 24): 
             d = int(h / 24)
        h = int(h % 24)
        return str(d) + "d " + str(h) + "h " + str(m) + "m " + str(r) + "s "  
    def get_price(self):
        d = 0.36 + self.seconds * 0.09
        s = "%8.2f" % d
        return s
    price = property(get_price)
    def get_total(self):
        return 100
    total = property(get_total)
