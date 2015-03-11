from django.db import models
from django.conf import settings
import requests


class FacebookEvent(models.Model):
    event_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1024)
    description = models.TextField()
    start_time = models.DateField()
    end_time = models.DateField()
    location = models.CharField(max_length=1024)

    @staticmethod
    def update_events(session, group_id):
        params = {
            'access_token': session.access_token,
            'since': 0,  # All events since epoch
        }
        events = requests.get("https://graph.facebook.com/v2.2/{}/events".format(settings.FACEBOOK_GROUP_ID),
                              params=params)
        pass


# Start a worker to update the event list every 5 minutes
pass


class FacebookSession(models.Model):
    SHORT_TOKEN_LENGTH = 10

    access_token = models.CharField(max_length=1024)

    def short_token(self):
        return self.access_token[:FacebookSession.SHORT_TOKEN_LENGTH] + "..."

    def is_valid(self):
        if self == self:
            return "Token valid as of {}".format("[now]")
        else:
            return "Token not valid."