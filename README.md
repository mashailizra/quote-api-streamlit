# Quote & Joke API
A FastAPI backend serving quotes from a local JSON file, with a 
Streamlit
frontend that consumes it. No database required.
## Status
In progress — Day 3/5 complete:  caching + tests.
## Tech stack
Python 3, FastAPI, Uvicorn, Streamlit, Requests
## Features (growing daily)
- [x] GET / — welcome message.
- [x] GET /quote/random — random quote from quotes.json.
- [x] GET /quotes?limit=N.
- [x] GET /quote/category/{category} (404    handled).
- [x] POST /quote — add a new quote (Pydantic-validated, 
persisted to quotes.json).
- [x] GET /quote/today — cached "quote of the day".
- [x] test_api.py — basic pass/fail checks against every endpoint.
## API docs
Once running, visit http://127.0.0.1:8000/docs for interactive 
API docs.