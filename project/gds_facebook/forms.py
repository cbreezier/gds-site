from django.forms.widgets import TextInput
from django.template.loader import render_to_string
from django.conf import settings


class FacebookAccessInput(TextInput):
    """
    Appends a Facebook Login button to the TextInput, so that an access token can be obtained by clicking the login
    button. Uses Facebook's Javascript SDK.
    """

    def render(self, name, value, attrs=None):
        attrs.update({'size': 120})
        return (TextInput.render(self, name, value, attrs) +
                render_to_string('facebook_login.html', {'app_id': settings.FACEBOOK_APP_ID}))
