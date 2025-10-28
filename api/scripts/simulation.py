import requests
import random
import time
from api.models import Times
from django.db import connection
from django.core.cache import cache

URL = r'http://127.0.0.1:8000/'  # replace with your url / usually localhost for development 
ENDPOINTS = ['books/', 'authors/']

def reset_db():
    """Clear the table Times and resets 'id' sequence"""
    Times.objects.all().delete()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='api_times';")

def sending_requests(number, use_cache = False):
    """Simple request simulation to simulate 'GET' requests with cache/without cache based on client request"""
    for request in range(number):
        endpoint = random.choice(ENDPOINTS)
        if endpoint == 'books/':
            url = URL + random.choice([endpoint + str(random.randint(1,23)), endpoint])
        elif endpoint == 'authors/':
            url = URL + random.choice([endpoint + str(random.randint(1,19)), endpoint])

        cache_key = f"resp:{url}"
        
        if use_cache:
            data = cache.get(cache_key)
            if not data:
                print("CACHE MISS:", url)
                response = requests.get(url)
                cache.set(cache_key, response.text, timeout=3)
            else:
                start_time = time.time()
                print("CACHE HIT:", url)
                response = data

                elapsed = time.time() - start_time
                Times.objects.create(
                    method = 'GET',
                    time=elapsed
                )
        else:
            response = requests.get(url)
            cache.delete(cache_key)

    print("Simulation complete")