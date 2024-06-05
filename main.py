import requests
from send_mail import send_mail

topic = "tesla"

url = "https://finance.yahoo.com"
apy_key = "de131c1538df43d59eec035fd3362a4a"

url = "https://newsapi.org/v2/everything?" \
       f"q={topic}&" \
       "from=2024-05-05&" \
       "sortBy=publishedAt&" \
       "apiKey=de131c1538df43d59eec035fd3362a4a&language=en" \


# Make request
request = requests.get(url)

#Get a disctionary with data
content = request.json()

#Access the articles titles
body = ""
for article in content["articles"]:
       body = ("Subject: Today's news"
                 + "\n" + body + (str(article["title"])
                 + "\n" + str(article["description"])
                 + "\n " + str(article["url"])
                 + 2*"\n"))

body = body.encode("utf-8")
send_mail(body)
print(body)