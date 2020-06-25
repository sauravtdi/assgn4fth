from django.core.management.base import BaseCommand
from user.models import User, ActivityPeriod
from mimesis.schema import Field
from mimesis import *
from mimesis.random import random as rn
from datetime import timedelta
import sys
import pytz


class Command(BaseCommand):
    args = "<arg1 arg2 ...>"
    help = "populate user table using mimesis library. please pass number of users to be created."

    def __init__(self):
        self.en = Person('en')
        self.dt = Datetime()
        self.ad = Address()
        self._ = Field('en')
        self.bs = Business()
        self.choice = Choice()

    def add_arguments(self, parser):
        # Positional arguments are standalone name
        parser.add_argument('user_number')

    def _create_user(self):
        first_name = self.en.name()
        last_name = self.en.last_name()
        full_name = first_name + ' ' + last_name
        email = self.en.email()
        email = first_name+'.'+last_name + \
            str(rn.randints(amount=1)[0])+'@'+email.split('@')[1]
        staff = self.choice(items=[True, False])
        timezone = self.choice(pytz.all_timezones)
        user = User(email=email, full_name=full_name,
                    timezone=timezone, password="S1234567s", staff=staff)
        user.set_password(user.password)
        user.save()
        return user, timezone

    def _create_activity(self, user, timezone):
        start_time = self.dt.datetime(start=2020, end=2020, timezone=timezone)
        interval = timedelta(seconds=rn.randints(1, a=1, b=59)[0], minutes=rn.randints(
            1, a=0, b=59)[0], hours=rn.randints(1, a=0, b=12)[0], days=rn.randints(1, a=0, b=1)[0])
        end_time = start_time + interval
        activity = ActivityPeriod(start_time=start_time, end_time=end_time,
                                  user=user)
        activity.save()

    def handle(self, *args, **options):
        for i in range(int(options['user_number'])):
            user, timezone = self._create_user()
            for r in range(self.choice([0, 1, 2, 3, 1])):
                self._create_activity(user, timezone)
        sys.stdout.write(
            "Successfully added {} users with random number of activities.".format(options['user_number']))
