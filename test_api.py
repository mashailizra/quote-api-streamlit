import requests

BASE_URL = "http://127.0.0.1:8000"

try:
    response = requests.get(f"{BASE_URL}/")

    assert response.status_code == 200

    print("GET /  PASS")

except AssertionError:
    print("GET /  FAIL")


try:
    response = requests.get(f"{BASE_URL}/quote/random")

    assert response.status_code == 200

    quote = response.json()

    assert "id" in quote
    assert "text" in quote
    assert "author" in quote
    assert "category" in quote

    print("GET /quote/random  PASS")

except AssertionError:
    print("GET /quote/random  FAIL")


try:
    response = requests.get(f"{BASE_URL}/quotes")

    assert response.status_code == 200

    quotes = response.json()

    assert isinstance(quotes, list)
    assert len(quotes) > 0

    for quote in quotes:
        assert "id" in quote
        assert "text" in quote
        assert "author" in quote
        assert "category" in quote

    print("GET /quotes  PASS")

except AssertionError:
    print("GET /quotes  FAIL")


try:
    response = requests.get(f"{BASE_URL}/quotes?limit=5")

    assert response.status_code == 200

    quotes = response.json()

    assert isinstance(quotes, list)
    assert len(quotes) <= 5

    print("GET /quotes?limit=5  PASS")

except AssertionError:
    print("GET /quotes?limit=5  FAIL")


try:
    response = requests.get(f"{BASE_URL}/quote/category/Motivation")

    assert response.status_code == 200

    quotes = response.json()

    assert isinstance(quotes, list)
    assert len(quotes) > 0

    for quote in quotes:
        assert quote["category"].lower() == "motivation"

    print("GET /quote/category/Motivation  PASS")

except AssertionError:
    print("GET /quote/category/Motivation  FAIL")


try:
    response = requests.get(
        f"{BASE_URL}/quote/category/ThisCategoryDoesNotExist"
    )

    assert response.status_code == 404

    print("GET /quote/category/invalid  PASS")

except AssertionError:
    print("GET /quote/category/invalid  FAIL")

try:
    response1 = requests.get(f"{BASE_URL}/quote/today")
    response2 = requests.get(f"{BASE_URL}/quote/today")

    assert response1.status_code == 200
    assert response2.status_code == 200

    quote1 = response1.json()
    quote2 = response2.json()

    assert "id" in quote1
    assert "text" in quote1
    assert "author" in quote1
    assert "category" in quote1

    assert quote1 == quote2

    print("GET /quote/today  PASS")

except AssertionError:
    print("GET /quote/today  FAIL")


try:
    new_quote = {
        "text": "Testing my Quote API",
        "author": "Test Author",
        "category": "Testing"
    }

    response = requests.post(
        f"{BASE_URL}/quote",
        json=new_quote
    )

    assert response.status_code == 200

    quote = response.json()

    assert "id" in quote
    assert "text" in quote
    assert "author" in quote
    assert "category" in quote

    assert quote["text"] == new_quote["text"]
    assert quote["author"] == new_quote["author"]
    assert quote["category"] == new_quote["category"]

    print("POST /quote  PASS")

except AssertionError:
    print("POST /quote  FAIL")


try:
    invalid_quote = {
        "text": "This quote is missing a category",
        "author": "Test Author"
    }

    response = requests.post(
        f"{BASE_URL}/quote",
        json=invalid_quote
    )

    assert response.status_code == 422

    print("POST /quote validation  PASS")

except AssertionError:
    print("POST /quote validation  FAIL")