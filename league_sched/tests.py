from django.test import TestCase
from league_sched.models import User

class AndrewTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="killself", karma=5.0, password="negative", sign_up_date="2016-07-21T18:50:58.434343Z")

    def test_animals_can_speak(self):
        test1 = User.objects.get(username="killself")
        self.assertEqual(test1.username, 'killself', msg="Received name {0}".format(test1.username))