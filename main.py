import requests

# Replace with your actual API key
API_URL = 'https://api.leakguardio.com/search/query'
API_KEY = 'your_api_key_here'

def get_data(search_term):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # Modify the URL with the search term
    response = requests.get(f"{API_URL}?search={search_term}", headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error: {response.status_code} - {response.text}')
        return None

if __name__ == "__main__":
    search_term = input("Enter search term: ")
    data = get_data(search_term)
    if data:
        print("Data retrieved successfully:")
        print(data)
