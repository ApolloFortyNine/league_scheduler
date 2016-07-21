# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from league_sched.models import User


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

    def update(selfself, instance, validated_data):
        pass
