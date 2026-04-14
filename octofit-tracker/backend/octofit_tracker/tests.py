from django.test import TestCase
from .models import UserProfile, Team, Activity, Workout, Leaderboard

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_userprofile_creation(self):
        team = Team.objects.create(name='Test Team')
        user = UserProfile.objects.create(name='Test User', email='test@example.com', team=team)
        self.assertEqual(str(user), 'Test User')

    def test_activity_creation(self):
        team = Team.objects.create(name='Test Team')
        user = UserProfile.objects.create(name='Test User', email='test@example.com', team=team)
        activity = Activity.objects.create(user=user, type='Run', duration=30)
        self.assertEqual(str(activity), 'Test User - Run')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy')
        self.assertEqual(str(workout), 'Pushups')

    def test_leaderboard_creation(self):
        team = Team.objects.create(name='Test Team')
        user = UserProfile.objects.create(name='Test User', email='test@example.com', team=team)
        leaderboard = Leaderboard.objects.create(user=user, score=100)
        self.assertEqual(str(leaderboard), 'Test User: 100')
