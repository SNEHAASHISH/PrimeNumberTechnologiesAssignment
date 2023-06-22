from django.core.management.base import BaseCommand
from appname.models import Restaurant

class Command(BaseCommand):
    help = 'Prints all restaurants'

    def handle(self, *args, **options):
        restaurants = Restaurant.objects.all()
        for restaurant in restaurants:
            print(restaurant.name)
            self.stdout.write(restaurant.name)
