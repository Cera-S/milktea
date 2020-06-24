import tkinter as tk
import requests
import config
import json

def formatData(data):
    endstr = ''

    for business in data['businesses']:
        businessInfo = ' %s \n Rating: %d \n' %(business['name'], business['rating'])
        endstr += businessInfo

    return endstr

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

    label['text'] = formatData(data)



root = tk.Tk()


canvas = tk.Canvas(root, height=667, width=375)
canvas.pack()

frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font='12')
entry.place(relwidth=0.65, relheight=0.4)

button = tk.Button(frame, text="Search", font=12, command=lambda: fetchData(entry.get()))
button.place(relx=0.7, relheight=0.4, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.85, relheight=0.95, anchor='n')


label = tk.Label(lower_frame)
label.place(relwidth=0.95, relheight=0.95)

root.mainloop()