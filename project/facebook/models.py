from django.db import models
import requests


class FacebookEvent(models.Model):
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