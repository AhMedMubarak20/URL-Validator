import requests

def validate_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return "Valid URL"
        else:
            return "Invalid URL"
    except requests.ConnectionError:
        return "Invalid URL"

url_to_validate = input("Enter URL to validate: ")
print(validate_url(url_to_validate))
