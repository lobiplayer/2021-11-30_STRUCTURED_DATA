import requests
import json

wordInTitle = input('Type the title (or word in title)')
author = input('Type the name of the author')

data = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={wordInTitle}+inauthor:{author}')

print(data) #gets a response 200

binary = data.content #gets the binary JSON file

output = json.loads(binary) #Transforms the JSON file into a python dictionary

print(output['totalItems']) #prints the total records

records = output['items']

for record in records:
    print(record['volumeInfo']['title'])
    print(record['volumeInfo']['authors'])
