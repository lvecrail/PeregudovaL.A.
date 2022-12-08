from tkinter import *

import requests
import json
import time

root = Tk()


def getUs(userName):
    url = f"https://github.com/apache/spark{userName}"

    return requests.get(url).json()


def st(value):
    file = open("gitParse.json", "w")
    file.writelines(json.dumps(value))


keys = [
    'company',
    'created_at',
    'email',
    'id',
    'name',
    'url'
]


def getData():
    userData = getUs

    n: dict = {}

    n['timestamp'] = time.time()

    for i in range(len(keys)):
        n[keys[i]] = userData[keys[i]]

    st(n)


root['bg'] = '#fafafa'

root.title('узнать данные')

root.geometry('300x250')

root.resizable(width=False, height=False)

frame_top = Frame(root, bg='#ffb700', bd=5)

frame_top.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.25)


frame_bottom = Frame(root, bg='#ffb700', bd=5)
frame_bottom.place(relx=0.15, rely=0.55, relwidth=0.7, relheight=0.1)


cityField = Entry(frame_top, bg='white', font=30)
cityField.pack()