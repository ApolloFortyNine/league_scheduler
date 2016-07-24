from django.test import TestCase
from league_sched.models import User, Team, TeamMember, AvailableTime

import random
from random import randrange
import string
import datetime
from datetime import timedelta, timezone
import pytz

class AndrewTestCase(TestCase):
    def setUp(self):
        # Generate numteam Teams and numteam Users and have the User be owner of the Team
        numteams = 400
        for x in range(0, numteams):
            user = self.random_user()
            team = self.random_teams(user)
            self.team_member(user, team)

        # Generate numaval times for teams
        numaval = 10
        allteams = Team.objects.all()
        for x in allteams:
            self.aval_time(x)


    def test_grab_user(self):
        allavals = AvailableTime.objects.all()
        print(allavals[0].start_time)
        print(allavals[0].end_time)
        self.assertEqual(allavals[0].team_id, '', msg="Received name {0}".format(allavals[0].team_id))

    def rand_datetime(self):
        secondsweek = 604800
        starttime = datetime.datetime.now(datetime.timezone.utc)
        endtime = datetime.datetime.now(datetime.timezone.utc) + timedelta(seconds=secondsweek)

        delta = endtime - starttime
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)

        randtime = starttime + timedelta(seconds=random_second)
        return randtime

    def rand_datetime_30min(self):
        secondsweek = 604800
        randtime = self.rand_datetime() + timedelta(seconds=secondsweek)

        hourrand = round(random.random()*23)
        minuterand = round(random.random()*1)
        randscaled = datetime.datetime(year=randtime.year, month=randtime.month, day=randtime.day, hour=hourrand, minute=1*30*minuterand)

        # randscaled.replace(tzinfo=timezone('UTC'))
        return pytz.utc.localize(randscaled)

    def random_user(self):
        newuser = {}
        newuser['username'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(15))
        newuser['sign_up_date'] = str(self.rand_datetime())
        newuser['password'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))
        newuser['karma'] = round(random.random()*10)

        user = User.objects.create(username=newuser['username'], sign_up_date=newuser['sign_up_date'], password=newuser['password'], karma=newuser['karma'])
        user.save()
        return user

    def random_teams(self, user):
        newteam = {}
        newteam['name'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(12))
        newteam['tag'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
        newteam['rating'] = round(random.random()*100)
        newteam['team_karma'] = round(random.random()*10)
        newteam['owner'] = user

        team = Team.objects.create(name=newteam['name'], tag=newteam['tag'], rating=newteam['rating'], team_karma=newteam['team_karma'], owner=newteam['owner'])
        team.save()
        return team

    def aval_time(self, team):
        newaval = {}
        startertime = self.rand_datetime_30min()
        endtime = startertime + timedelta(hours=4)
        newaval['start_time'] = str(startertime)
        newaval['end_time'] = str(endtime)
        newaval['team_id'] = team

        aval = AvailableTime.objects.create(start_time=newaval['start_time'], end_time=newaval['end_time'], team_id=newaval['team_id'])
        aval.save()
        return aval

    def team_member(self, user, team):
        teammember = TeamMember.objects.create(user=user, team=team)
        teammember.save()
        return teammember