from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from league_sched.models import User, LeagueName, Team, TeamMember, FutureMatch
from league_sched.models import AvailableTime, CompletedMatch
from league_sched.serializers import UserSerializer, LeagueNameSerializer, TeamSerializer
from league_sched.serializers import TeamMemberSerializer, FutureMatchSerializer
from league_sched.serializers import AvailableTimeSerializer, CompletedMatchSerializer


# TODO Change generic lists to either limit return or to only create
###########################
# The graveyard belows serves as a reminder as to why you should always read
# the entire tutorial before starting a project
###########################

# @api_view(['GET', 'POST'])
# def user_list(request, format=None):
#     if request.method == 'GET':
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def user_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a user instance.
#     """
#     try:
#         user = User.objects.get(pk=pk)
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def league_name_detail(request, pk, format=None):
#     if request.method == 'POST':
#         serializer = LeagueNameSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     try:
#         league_name = LeagueName.objects.get(pk=pk)
#     except LeagueName.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         league_name = LeagueName.objects.get(pk=pk)
#         serializer = LeagueNameSerializer(league_name)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = LeagueNameSerializer(league_name, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         league_name.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


###################
# Mixins example
###################

# class LeagueNameDetail(generics.GenericAPIView,
#                        mixins.RetrieveModelMixin):
#     queryset = LeagueName.objects.all()
#     serializer_class = LeagueNameSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)


class LeagueNameDetail(generics.RetrieveUpdateDestroyAPIView,
                       generics.CreateAPIView):
    queryset = LeagueName.objects.all()
    serializer_class = LeagueNameSerializer


# TODO Create a different endpoint to see top X teams
class TeamDetail(generics.RetrieveUpdateDestroyAPIView,
                 generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


# class TeamToUsernameDetail(generics.RetrieveUpdateDestroyAPIView,
#                            generics.CreateAPIView):
#     queryset = TeamToUsername
#     serializer_class = TeamToUsernameSerializer


class TeamMemberDetail(generics.RetrieveUpdateDestroyAPIView,
                       generics.CreateAPIView):
    queryset = TeamMember
    serializer_class = TeamMemberSerializer


class FutureMatchDetail(generics.RetrieveUpdateDestroyAPIView,
                        generics.CreateAPIView):
    queryset = FutureMatch
    serializer_class = FutureMatchSerializer


class AvailableTimeDetail(generics.RetrieveUpdateDestroyAPIView,
                          generics.CreateAPIView):
    queryset = AvailableTime
    serializer_class = AvailableTimeSerializer


class CompletedMatchDetail(generics.RetrieveUpdateDestroyAPIView,
                     generics.CreateAPIView):
    queryset = CompletedMatch
    serializer_class = CompletedMatchSerializer
