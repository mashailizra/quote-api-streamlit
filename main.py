import json
import random
from datetime import date
from functools import lru_cache

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Quote(BaseModel):
    id: int
    text: str
    author: str
    category: str

class NewQuote(BaseModel):
    text: str
    author: str
    category: str

app= FastAPI()

@app.get("/")
def welcome():
    return {"message":"Welcome to the Quote & Joke API !"}


@app.get("/quote/random",response_model=Quote)
def random_quote():
    with open("quotes.json","r")as file:
        quotes=json.load(file)

    return random.choice(quotes)

@app.get("/quotes", response_model=list[Quote])
def get_quotes(limit: int | None = None):
    with open("quotes.json", "r") as file:
        quotes = json.load(file)

    if limit is None:
        return quotes

    return quotes[:limit]

@app.get("/quote/category/{category}", response_model=list[Quote])
def get_quotes_by_category(category: str):
    with open("quotes.json", "r") as file:
        quotes = json.load(file)

    matching_quotes = [
        quote for quote in quotes
        if quote["category"].lower() == category.lower()
    ]

    if not matching_quotes:
        raise HTTPException(
            status_code=404,
            detail=f"Category '{category}' not found"
        )

    return matching_quotes


@app.post("/quote", response_model=Quote)
def create_quote(new_quote: NewQuote):
    with open("quotes.json", "r") as file:
        quotes = json.load(file)

    new_id = max(quote["id"] for quote in quotes) + 1

    quote = Quote(
        id=new_id,
        text=new_quote.text,
        author=new_quote.author,
        category=new_quote.category
    )

    quotes.append(quote.model_dump())

    with open("quotes.json", "w") as file:
        json.dump(quotes, file, indent=4)

    return quote

@lru_cache
def get_daily_quote(date_key: str):
    with open("quotes.json", "r") as file:
        quotes = json.load(file)

    index = sum(ord(char) for char in date_key) % len(quotes)

    return quotes[index]

@app.get("/quote/today",response_model=Quote)
def quote_of_the_day():
    today =date.today().isoformat()

    return get_daily_quote(today)