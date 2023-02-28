import requests
from requests.exceptions import HTTPError


print("Print each key-value pair from JSON response")
for key, value in jsonResponse.items():
    print(key, ":", value)