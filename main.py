import requests
from email_news import send_email
import os

topic = ("tesla")
api_key = os.getenv("News_API_key")

url = ("https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2025-05-16&to=2025-05-16&" \
       "sortBy=popularity&language=en&" \
       f"apiKey={api_key}")

# Make a request
request= requests.get(url)

# Make a dictionary with data
content = request.json()

body =""
for article in content["articles"][0:10]:
    if article["title"] and article["url"] is not None:
        body = (body + f"""Title: {str(article["title"])}""" +"\n" \
                + f"""Description: {str(article["description"])}""" \
                +"\n"+ f"""Check here: {str(article["url"])}""" + "\n\n" )


body = body.strip().encode("utf-8")
send_email(body)