from datetime import datetime, timedelta
from django.db import models
from django.urls import reverse

class Call(models.Model):
    timestampstart = models.DateTimeField(verbose_name='Start')
    timestampend = models.DateTimeField(verbose_name='End',null=True,blank=True)
    source = models.CharField(verbose_name='Source',max_length=11)
    destination = models.CharField(verbose_name='Destination',max_length=11)
    def get_call_id(self): 
        return self.id
    call_id = property(get_call_id)
    def get_type(self):
        if self.timestampend is not None:
            return 1
        else:
            return 2
        return t
    type = property(get_type)
    def get_secondschargebyday(self, tss, tse):
        if tss.hour < 6:
            if tse.hour < 6:
                s = 0
            else:
                if tse.hour < 22:
                    s = (tse-datetime(tss.year, tss.month, tss.day, 6, 0)).total_seconds()
                else:
                    s = (datetime(tse.year, tse.month, tse.day, 22, 0)-datetime(tss.year, tss.month, tss.day, 6, 0)).total_seconds()
        else:
            if tse.hour > 22:
                if tss.hour >= 22:
                    s = 0
                else:
                    s = (datetime(tse.year, tse.month, tse.day, 22, 0)-tss).total_seconds()
            else:
                s = (tse-tss).total_seconds()
        return s        
    def get_secondscharge(self):
        s = 0
        tss = self.timestampstart
        tse = self.timestampend
        while True:
            if ((datetime(tse.year, tse.month, tse.day, 0, 0)-datetime(tss.year, tss.month, tss.day, 0, 0)).total_seconds()/60/60/24 > 0):
                s += self.get_secondschargebyday(tss, datetime(tss.year, tss.month, tss.day, 23, 59))
            else:
                s += self.get_secondschargebyday(tss, tse)
                break
            tss = datetime(tss.year, tss.month, tss.day, 0, 0) + timedelta(days=1)     
        return s
    secondscharge = property(get_secondscharge)
    def get_seconds(self):
        s = int((self.timestampend-self.timestampstart).total_seconds())
        return s
    seconds = property(get_seconds)
    def get_hours(self):
        s = self.seconds
        h = s // 3600
        return h
    hours = property(get_hours)
    def get_duration(self):
        s = self.seconds
        h = self.hours
        d = h // 86400
        r = s % 3600
        m = r // 60
        r = r % 60
        if (h >= 24): 
             d = int(h / 24)
        h = int(h % 24)
        return str(d) + "d " + str(h) + "h " + str(m) + "m " + str(r) + "s "  
    duration = property(get_duration)
    def get_price(self):
        d = 0.36 + int(self.secondscharge/60) * 0.09
        s = "%8.2f" % d
        return s
    price = property(get_price)
