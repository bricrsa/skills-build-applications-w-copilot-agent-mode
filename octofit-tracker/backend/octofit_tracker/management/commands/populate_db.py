from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create users
        users = [
            User(email='thundergod@mhigh.edu', name='Thunder God', age=30),
            User(email='metalgeek@mhigh.edu', name='Metal Geek', age=25),
            User(email='zerocool@mhigh.edu', name='Zero Cool', age=22),
            User(email='crashoverride@hmhigh.edu', name='Crash Override', age=28),
            User(email='sleeptoken@mhigh.edu', name='Sleep Token', age=35),
        ]
        User.objects.bulk_create(users)

        # Create teams
        teams = [
            Team(name='Blue Team', members=[user.email for user in users[:3]]),
            Team(name='Gold Team', members=[user.email for user in users[3:]]),
        ]
        Team.objects.bulk_create(teams)

        # Create activities
        activities = [
            Activity(user=users[0].email, type='Cycling', duration=60),
            Activity(user=users[1].email, type='Crossfit', duration=120),
            Activity(user=users[2].email, type='Running', duration=90),
            Activity(user=users[3].email, type='Strength', duration=30),
            Activity(user=users[4].email, type='Swimming', duration=75),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard entries
        leaderboard_entries = [
            Leaderboard(user=users[0].email, points=100),
            Leaderboard(user=users[1].email, points=90),
            Leaderboard(user=users[2].email, points=95),
            Leaderboard(user=users[3].email, points=85),
            Leaderboard(user=users[4].email, points=80),
        ]
        Leaderboard.objects.bulk_create(leaderboard_entries)

        # Create workouts
        workouts = [
            Workout(name='Cycling Training', description='Training for a road cycling event'),
            Workout(name='Crossfit', description='Training for a crossfit competition'),
            Workout(name='Running Training', description='Training for a marathon'),
            Workout(name='Strength Training', description='Training for strength'),
            Workout(name='Swimming Training', description='Training for a swimming competition'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))