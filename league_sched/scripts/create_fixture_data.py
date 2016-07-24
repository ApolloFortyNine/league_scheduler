import random
from random import randrange
import string
import datetime
import os
from datetime import timedelta

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "league_scheduler.settings")
django.setup()
from league_sched.models import User, Team


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
    return randTime




def randomUser():
    newUser = {}
    newUser['username'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
    newUser['sign_up_date'] = str(randDatetime())
    newUser['password'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    newUser['karma'] = round(random.random()*10)

    user = User.objects.create(username=newUser['username'], sign_up_date=newUser['sign_up_date'], password=newUser['password'], karma=newUser['karma'])
    user.save()
    return user


def randomTeams(users):
    newTeam = {}
    newTeam['name'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
    newTeam['tag'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
    newTeam['rating'] = round(random.random()*100)
    newTeam['team_karma'] = round(random.random()*10)
    newTeam['owner'] = users[round(random()*5)]

    User.objects.create(name=newTeam['name'], tag=newTeam['tag'], rating=newTeam['rating'], team_karma=newTeam['team_karma'], owner=newTeam['owner'])


numTeams = 400
for x in range(0, numTeams):
    users = []
    for y in range(0, 5):
        users.append(randomUser())
    randomTeams(users)
