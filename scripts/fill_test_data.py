# from django.conf import settings
# settings.configure()
#
# import os
# import sys
#
# from django.core.wsgi import get_wsgi_application
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'league_scheduler.settings'
# application = get_wsgi_application()

import random
import time

from django.conf import settings
settings.configure()
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.core.management.base import BaseCommand
from league_sched import models



def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

print(randomDate("1/1/2008 1:30 PM", "1/1/2009 4:50 AM", random.random()))



quit()

new_entry = models.User(name='me', age='222', about='stackoverflow')
new_entry.save()