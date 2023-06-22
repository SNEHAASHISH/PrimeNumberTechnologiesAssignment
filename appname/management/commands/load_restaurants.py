import csv
from django.core.management.base import BaseCommand
from appname.models import Restaurant


class Command(BaseCommand):
    help = 'Load restaurant data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    restaurant = Restaurant.objects.create(
                        id=row['id'],
                        name=row['name'],
                        location=row['location'],
                        items=row['items'],
                        lat_log=row['lat_log'],
                        full_details=row['full_details'],
                    )
                    print('Restaurant created:', restaurant)
                except KeyError:
                    self.stdout.write(self.style.WARNING('Skipping row with missing fields: {}'.format(row)))

        self.stdout.write(self.style.SUCCESS('Data loaded successfully.'))
