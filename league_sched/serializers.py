# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from league_sched.models import User, LeagueName


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
