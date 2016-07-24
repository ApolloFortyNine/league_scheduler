from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    sign_up_date = models.DateTimeField()
    password = models.CharField(max_length=64)
    karma = models.DecimalField(max_digits=10, decimal_places=3)


class LeagueName(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Check if unique id is given so we don't have to worry about name changes (someone else owning the name)
    league_name = models.CharField(max_length=30)
    verified = models.BooleanField(default=0)


class Team(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=5)
    # Probably has to be stored separately (RD and actual rating)
    rating = models.DecimalField(max_digits=14, decimal_places=5)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    team_karma = models.DecimalField(max_digits=10, decimal_places=3)


class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)


class FutureMatch(models.Model):
    match_date = models.DateTimeField()
    # Probably shouldn't allow people to delete teams if one is planned. Than delete and inform manually
    team_1 = models.ForeignKey(Team, related_name="futurematch_team_1")
    team_2 = models.ForeignKey(Team, related_name="futurematch_team_2")
    # "R" or "B"
    side = models.CharField(max_length=1)


class AvailableTime(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    team_id = models.ForeignKey(Team)


class CompletedMatch(models.Model):
    match_date = models.DateTimeField()
    # Allow matches to exist in history even if team is deleted
    team_1 = models.ForeignKey(Team, related_name="completedmatch_team_1", db_constraint=False)
    team_2 = models.ForeignKey(Team, related_name="completedmatch_team_2", db_constraint=False)
    # Which side was red to begin
    starting_team = models.ForeignKey(Team, related_name="completedmatch_starting_team", db_constraint=False)
    gold_1 = models.IntegerField()
    gold_2 = models.IntegerField()
    dragon_1 = models.SmallIntegerField()
    dragon_2 = models.SmallIntegerField()
    baron_1 = models.SmallIntegerField()
    baron_2 = models.SmallIntegerField()
    tower_1 = models.SmallIntegerField()
    tower_2 = models.SmallIntegerField()
    kills_1 = models.SmallIntegerField()
    kills_2 = models.SmallIntegerField()
    elo_changed_1 = models.SmallIntegerField()
    elo_changed_2 = models.SmallIntegerField()