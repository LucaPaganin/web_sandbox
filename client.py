import requests


n_reqs = 10
url = "http://localhost:8888/"

for i in range(n_reqs):
    print(f"Sending request {i+1}")
    requests.get(url)