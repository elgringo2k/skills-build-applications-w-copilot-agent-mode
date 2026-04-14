from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Example models (should be replaced with actual models in your app)
from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        octo_models.Team.objects.all().delete()
        octo_models.UserProfile.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Create Teams
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Create Users
        ironman = octo_models.UserProfile.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = octo_models.UserProfile.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        batman = octo_models.UserProfile.objects.create(name='Batman', email='batman@dc.com', team=dc)
        superman = octo_models.UserProfile.objects.create(name='Superman', email='superman@dc.com', team=dc)

        # Create Activities
        octo_models.Activity.objects.create(user=ironman, type='run', duration=30)
        octo_models.Activity.objects.create(user=batman, type='cycle', duration=45)

        # Create Workouts
        octo_models.Workout.objects.create(name='Pushups', description='Standard pushups', difficulty='Easy')
        octo_models.Workout.objects.create(name='Squats', description='Bodyweight squats', difficulty='Medium')

        # Create Leaderboard
        octo_models.Leaderboard.objects.create(user=ironman, score=100)
        octo_models.Leaderboard.objects.create(user=batman, score=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
