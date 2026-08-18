import json
import random

from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def welcome():
    return {"message":"Welcome to the Quote & Joke API !"}


@app.get("/quote/random")
def random_quote():
    with open("quotes.json","r")as file:
        quotes=json.load(file)

    return random.choice(quotes)
