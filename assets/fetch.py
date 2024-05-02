import requests
import os

def fetch_wakatime_data():
    wakatime_api_key = os.getenv('WAKATIME_API_KEY')
    headers = {
        'Authorization': f'Bearer {wakatime_api_key}'
    }
    
    # Make API request to retrieve Wakatime statistics
    response = requests.get('https://wakatime.com/api/v1/users/current/stats/last_7_days', headers=headers)
    data = response.json()

    # Process data and update README (example)
    # Write the fetched data to a README file
    with open('README.md', 'w') as f:
        f.write(f'## Wakatime Statistics\n\n')
        f.write(f'Total coding time: {data["data"]["total_seconds"]} seconds\n')

if __name__ == '__main__':
    fetch_wakatime_data()
