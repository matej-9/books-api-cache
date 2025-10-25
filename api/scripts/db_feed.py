from api.models import Times, Book, Author
import pandas as pd
import requests
from django.db import connection

def reset_db():
    """Clear the table Book and resets 'id' sequence"""
    Book.objects.all().delete()
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='api_book';")

def book_scraper(url):
    """Scraper for getting books to feed our DB runned with script *python manage.py runscript db_feed*"""
    Book.objects.all().delete()
    headers = {
    "User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    book_tables = pd.read_html(response.text)
    book_df = book_tables[1]
    book_df.columns = book_df.columns.str.strip()

    for _, row in book_df.iterrows():
        try:
            new_book = Book.objects.create(title = row['Book'],
            year = row['First published'])
            authors_str = row.get('Author(s)', '')
            if pd.isna(authors_str) or authors_str.strip() == '':
                authors_objs = []
            else:
                authors_names = [name.strip() for name in authors_str.split(',')]
                authors_objs = [Author.objects.get_or_create(name=name)[0] for name in authors_names]

            new_book.authors.set(authors_objs)
        except Exception as e:
            print(f'Error: {e}')
    

reset_db()
book_scraper(r'https://en.wikipedia.org/wiki/List_of_best-selling_books')

# python manage.py runscript db_feed