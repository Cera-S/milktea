import requests
import json
import config
import sys
from json2html import *

# making the api call
def fetchData(userInput):
    # create object
    API_KEY = config.api_key
    ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
    HEADERS = {'Authorization': 'bearer %s' % API_KEY}
    PARAMETERS = {'term': 'boba',
                'limit': 25,
                'location': '%s' %userInput} # 'key': 'value'

    # make request to yelp API
    response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)

    data = response.json()
 
    # converting to json string
    dataString = json.dumps(data)

    for business in data['businesses']:
        print(business['name'])
        print ("Rating:", business['rating'], "\n")

    # prompt user
    yn = input ("Would you like this printed to an HTML file? (Y/N) \n → ")

    if yn == "Y" or "y":
        print ("loading file...")
        htmlFile(userInput, dataString)
    else:
        exit(0)


# creating the new output file
def htmlFile(userInput, dataString):
    htmlTable = json2html.convert(json = dataString)

    with open('boba.html', 'w') as f:
        f.write(htmlTable)
        f.close()
