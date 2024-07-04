import http.client

conn = http.client.HTTPSConnection("aeona3.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "5b8c88a3famshe98e5b0bb78b853p1213d1jsndbacd4761e4a",
    'X-RapidAPI-Host': "aeona3.p.rapidapi.com"
}

conn.request("GET", "/?text=%3CREQUIRED%3E&userId=12312312312", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))