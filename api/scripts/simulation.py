import requests
import random
from api.models import Times
from django.db import connection

URL = r'http://127.0.0.1:8000/'  # replace with your url / usually localhost for development 
ENDPOINTS = ['books/', 'authors/']

def reset_db():
    """Clear the table Times and resets 'id' sequence"""
    Times.objects.all().delete()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='api_times';")

def sending_requests(number):
    """Simple request simulation to simulate 'GET' requests"""
    for request in range(number):
        endpoint = random.choice(ENDPOINTS)
        if endpoint == 'books/':
            url = URL + random.choice([endpoint + str(random.randint(0,200)), endpoint])
        elif endpoint == 'authors/':
            url = URL + random.choice([endpoint + str(random.randint(0,19)), endpoint])
        response = requests.get(url)
    print("Simulation complete")

reset_db()
sending_requests(100) # replace with number of requests required

# python manage.py runscript simulation