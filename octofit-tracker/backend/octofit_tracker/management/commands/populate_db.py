from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # TODO: Implement test data creation for users, teams, activities, leaderboard, workouts
        self.stdout.write(self.style.SUCCESS('Test data population not yet implemented.'))
