import requests
import json
import config

print("Boba Locator (´∀｀)♡")

# handle user input
location = input("Enter your location: ")

# create object
API_KEY = config.api_key
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'bearer %s' % API_KEY}
PARAMETERS = {'term': 'boba',
            'limit': 25,
            'location': '%s' %location} # 'key': 'value'

# make request to yelp API
response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

data = response.json()

for business in data['businesses']:
    print(business['name'])
    print ("Rating:", business['rating'], "\n")