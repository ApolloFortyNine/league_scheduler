# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from league_sched.models import User, LeagueName, Team, TeamMember
from league_sched.models import FutureMatch, AvailableTime, CompletedMatch


class UserSerializer(serializers.ModelSerializer):
    # username = models.CharField(max_length=30)
    # sign_up_date = models.DateTimeField()
    # password = models.CharField(max_length=64)
    # karma = models.DecimalField(max_digits=5, decimal_places=5)
    class Meta:
        model = User
        fields = ('id', 'username', 'sign_up_date', 'password', 'karma')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance


class LeagueNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeagueName
        fields = '__all__'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


# class TeamToUsernameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = TeamToUsername
#         fields = '__all__'


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class FutureMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = FutureMatch
        fields = '__all__'


class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = '__all__'


class CompletedMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedMatch
        fields = '__all__'
