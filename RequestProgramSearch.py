import requests
import json

data = requests.get('https://www.googleapis.com/books/v1/volumes?q=vinci+inauthor:brown')

print(data) #gets a response 200

binary = data.content #gets the binary JSON file

output = json.loads(binary) #Transforms the JSON file into a python dictionary

print(output['totalItems']) #prints the total records

records = output['items']

for record in records:
    print(record['volumeInfo']['title'])
    print(record['volumeInfo']['authors'])
