from django.shortcuts import render
import requests

# Create your views here.

API_KEY = "5aa3c26ba6cf877fcde06a325c127e2d"
BASE_URL = "https://gnews.io/api/v4/top-headlines"

COUNTRIES = {
    "USA": "us",
    "India": "in",
    "UK": "gb",
    "Canada": "ca",
    "Australia": "au",
    "Germany": "de",
    "France": "fr",
    "Italy": "it",
}

CATEGORIES = ["general", "business", "entertainment", "health", "science", "sports", "technology"]

def home(request):
    selected_country = request.GET.get("country", "us")
    selected_category = request.GET.get("category", "general")
    search_query = request.GET.get("q", "")

    params = {
        "apikey": API_KEY,
        "max": 10
    }

    if search_query:
        params["q"] = search_query
    else:
        params["country"] = selected_country
        params["topic"] = selected_category

    response = requests.get(BASE_URL, params=params)
    data = response.json()
    articles = data.get("articles", [])

    context = {
        "articles": articles,
        "countries": COUNTRIES,
        "categories": CATEGORIES,
        "selected_country": selected_country,
        "selected_category": selected_category,
        "search_query": search_query,
    }
    return render(request, "news/home.html", context)