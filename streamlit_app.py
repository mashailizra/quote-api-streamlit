import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("Quote & Joke API")

try:
    response = requests.get(f"{API_URL}/quote/today")

    response.raise_for_status()

    quote = response.json()

    st.subheader("Quote of the Day")
    st.write(f'"{quote["text"]}"')
    st.write(f'— {quote["author"]}')
    st.write(f'Category: {quote["category"]}')

except requests.exceptions.ConnectionError:
    st.error("Is the API running? Please start FastAPI on port 8000.")


if st.button("Get Random Quote"):
    try:
        response = requests.get(f"{API_URL}/quote/random")

        response.raise_for_status()

        random_quote = response.json()

        st.subheader("Random Quote")
        st.write(f'"{random_quote["text"]}"')
        st.write(f'— {random_quote["author"]}')
        st.write(f'Category: {random_quote["category"]}')

    except requests.exceptions.ConnectionError:
        st.error("Is the API running? Please start FastAPI on port 8000.")


st.subheader("Browse by Category")

try:
    response = requests.get(f"{API_URL}/quotes")

    response.raise_for_status()

    quotes = response.json()

    categories = list({quote["category"] for quote in quotes})

    selected_category = st.selectbox(
        "Choose a category",
        categories
    )

    filtered_quotes = [
        quote
        for quote in quotes
        if quote["category"] == selected_category
    ]

    for quote in filtered_quotes:
        st.write(f'"{quote["text"]}"')
        st.write(f'— {quote["author"]}')
        st.write("---")

except requests.exceptions.ConnectionError:
    st.error("Is the API running? Please start FastAPI on port 8000.")


st.subheader("Add a New Quote")

with st.form("add_quote_form"):
    quote_text = st.text_input("Quote")
    quote_author = st.text_input("Author")
    quote_category = st.text_input("Category")

    submitted = st.form_submit_button("Add Quote")

    if submitted:
        if not quote_text.strip() or not quote_author.strip() or not quote_category.strip():
            st.warning("Please fill in all three fields.")

        else:
            try:
                new_quote = {
                    "text": quote_text,
                    "author": quote_author,
                    "category": quote_category
                }

                response = requests.post(
                    f"{API_URL}/quote",
                    json=new_quote
                )

                response.raise_for_status()

                st.success("Quote added successfully!")

                

            except requests.exceptions.ConnectionError:
                st.error("Is the API running? Please start FastAPI on port 8000.")