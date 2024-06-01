import requests

url = "https://finance.yahoo.com"
apy_key = "de131c1538df43d59eec035fd3362a4a"

url = "https://newsapi.org/v2/everything?q=tesla&from=" \
       "2024-05-01&sortBy=" \
       "publishedAt&apiKey=de131c1538df43d59eec035fd3362a4a"

# Make request
request = requests.get(url)

#Get a disctionary with data
content = request.json()

#Access
for article in content["articles"]:
       print(article["title"])
       print(article["description"])

print(content)