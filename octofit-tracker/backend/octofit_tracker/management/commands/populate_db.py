from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, User, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data (delete individually for Djongo compatibility)
        for obj in Leaderboard.objects.exclude(id=None):
            obj.delete()
        for obj in Activity.objects.exclude(id=None):
            obj.delete()
        for obj in Workout.objects.exclude(id=None):
            obj.delete()
        for obj in User.objects.exclude(id=None):
            obj.delete()
        for obj in Team.objects.exclude(id=None):
            obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
            User(name='Batman', email='batman@dc.com', team=dc),
        ]
        for user in users:
            user.save()

        # Create activities
        Activity.objects.create(user=users[0], type='Running', duration=30, date='2025-12-01')
        Activity.objects.create(user=users[1], type='Cycling', duration=45, date='2025-12-02')
        Activity.objects.create(user=users[2], type='Swimming', duration=60, date='2025-12-03')
        Activity.objects.create(user=users[3], type='Yoga', duration=20, date='2025-12-04')

        # Create workouts
        workout1 = Workout.objects.create(name='Hero Endurance', description='Endurance workout for heroes')
        workout2 = Workout.objects.create(name='Power Training', description='Strength workout for heroes')
        workout1.suggested_for.add(marvel, dc)
        workout2.suggested_for.add(marvel, dc)

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
