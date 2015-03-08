from django.db import models


class FacebookAccessToken(models.Model):
    access_token = models.CharField(max_length=1024)

    def short_token(self):
        return self.access_token[:10] + "..."

    def is_valid(self):
        if self == self:
            return "Token valid as of {}".format("[now]")
        else:
            return "Token not valid."