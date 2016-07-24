import random
from random import randrange
import string
import datetime
import os
from datetime import timedelta

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "league_scheduler.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from league_sched import models


# models.User.objects.all().delete()
# quit()

def randDatetime():
    secondsInAWeek = 604800
    startTime = datetime.datetime.now(datetime.timezone.utc)
    endTime = datetime.datetime.now(datetime.timezone.utc) + timedelta(seconds=secondsInAWeek)

    delta = endTime - startTime
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)

    randTime = startTime + timedelta(seconds=random_second)
    print(randTime)
    return randTime




def randomUser():
    newUser = {}
    newUser['username'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
    newUser['sign_up_date'] = str(randDatetime())
    newUser['password'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    newUser['karma'] = round(random.random()*10)

    models.User.objects.create(username=newUser['username'], sign_up_date=newUser['sign_up_date'], password=newUser['password'], karma=newUser['karma'])


def randomUser():
    newUser = {}
    newUser['username'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
    newUser['sign_up_date'] = str(randDatetime())
    newUser['password'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    newUser['karma'] = round(random.random()*10)

    models.User.objects.create(username=newUser['username'], sign_up_date=newUser['sign_up_date'], password=newUser['password'], karma=newUser['karma'])


numTeams = 400
for x in range(0, numTeams):
    for y in range(0, 5):
        randomUser()
    randomTeams()