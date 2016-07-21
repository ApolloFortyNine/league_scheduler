from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from league_sched.models import User
from league_sched.serializers import UserSerializer


@api_view(['GET', 'POST'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
