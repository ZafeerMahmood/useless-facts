import requests

def fetch_useless_fact():
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        response.raise_for_status()  # Raise an HTTPError for bad responses
        data = response.json()
        print(data['text'])
    except requests.exceptions.RequestException as error:
        print(error)
fetch_useless_fact()
print('ending...')
