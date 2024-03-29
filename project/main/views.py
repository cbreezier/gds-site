from django.shortcuts import render
import requests

TEMP_ACCESS_TOKEN = 'CAACEdEose0cBAFj3J4KFxZAJyMoR90iBQ5KPjrQun5ZCfzqivnMZA3UYTDjyYfKhkcUVapjCF9mxXgZBgkaEoWnyH5ag4CYlrnZAChXgBrnNcMnvoJKjtvxpxH87qSVLSeCb8rA4Iq1yQykYutdVfQ535ZBid7kjJldgvJWGZCv6jcxKPl5JHtdL15NsHRudS52lYrkzOzlrMhVmuATraBvXtbPUXZCzJLoZD'


def home(request):
    return render(request, 'home.html')


def get_events(request):
    params = {
        'access_token': TEMP_ACCESS_TOKEN,
        'since': 0
    }
    data = requests.get('https://graph.facebook.com/185233411589007/events', params=params)
    events = data.json()['data']
    return render(request, 'events.html', {'events': events})


def contact(request):
    return render(request, 'contact.html')


def resources(request):
    return render(request, 'resources.html')