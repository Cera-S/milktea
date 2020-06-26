import tkinter as tk
import requests
import config
import json

def formatData(data):
    endstr = ''
    try:
        for business in data['businesses']:
            businessInfo = ' %s \n Rating: %d \n \n' %(business['name'], business['rating'])
            endstr += businessInfo
    
    except:
        return "Invalid location, please re-enter."
    
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

def forward():
    return


def prev():
    return

root = tk.Tk()

title = tk.Label(root, text="Boba Tracker", font='24')
title.grid(row=0, column=0, columnspan=3)

canvas = tk.Canvas(root, height=720, width=1200, bg='#f7e3af')
canvas.grid(row=2, column=1)

frame = tk.Frame(root, bg='#f7e3af')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font='12')
entry.place(relwidth=0.5, relheight=0.4)

button = tk.Button(frame, text="Search", font=12, command=lambda: fetchData(entry.get()))
button.place(relx=0.55, relheight=0.4, relwidth=0.2)

lower_frame = tk.Frame(root, bd=5)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.65, anchor='n')

button = tk.Button(frame, text="Export Data", font=12)
button.place(relx=0.55, rely=0.55, relheight=0.4, relwidth=0.2)


buttonPrev = tk.Button(root, text="<<", command=prev)
buttonMid = tk.Button(root, text="Exit", command=root.quit)
buttonForward = tk.Button(root, text=">>", command=lambda: forward(2))

buttonPrev.grid(row=3, column=0)
buttonMid.grid(row=3, column=1)
buttonForward.grid(row=3, column=2)

label = tk.Label(lower_frame, bg='#f3eec3')
label.pack(relwidth=1, relheight=1)

root.mainloop()