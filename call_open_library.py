import requests

isbn = '9780816530731'

isbn_url = f'https://openlibrary.org/isbn/{isbn}.json'
isbn_response = requests.get(isbn_url)
isbn_json = isbn_response.json()

# Get book title, publisher & publication year.
title = isbn_json['title']
publisher = isbn_json['publishers'][0]
pub_year = isbn_json['publish_date']

work_key = isbn_json['works'][0]['key']
work_url = f'https://openlibrary.org{work_key}.json'
work_json = requests.get(work_url).json()

#Get book summary
summary = work_json['description']['value']

author_key = work_json['authors'][0]['author']['key']
author_url = f'https://openlibrary.org{author_key}.json'
author_json = requests.get(author_url).json()

#Get author name, birth date, and death date
author_name_split = author_json['personal_name'].split(' ')
author_firstname = author_name_split[0]
author_surname = author_name_split[1]
author_birth_date = author_json['birth_date'][-4:]
author_death_date = author_json['death_date'][-4:]

ol_lookup = {
    'ISBN': isbn,
    'title': title,
    'author': (author_firstname, author_surname),
    'author_life': (author_birth_date, author_death_date),
    'publisher': publisher,
    'year': pub_year,
    'summary': summary
}

print(ol_lookup)
