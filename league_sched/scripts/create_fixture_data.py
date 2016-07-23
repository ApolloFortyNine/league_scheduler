import random
import json
import time
import string
import datetime
import pytz

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

    str(datetime.datetime.now(datetime.timezone.utc))
    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)




def randomUser(pkUser):
    newUser = {}
    newUser['username'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
    newUser['sign_up_date'] = str(datetime.datetime.now(datetime.timezone.utc))
    newUser['password'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    newUser['karma'] = round(random.random()*10)

    modelObj = {}
    modelObj['model'] = "league_sched.User"
    modelObj['pk'] = pkUser
    modelObj['fields'] = newUser

    pkUser += 1
    return modelObj


numUsers = 10
randUsers = []
for x in range(1, numUsers+1):
    randUsers.append(randomUser(x))


with open('data.json', 'w') as outfile:
    json.dump(randUsers, outfile)