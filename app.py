import requests
import time
from datetime import datetime

def check_website():
    url = "https://miusoft.info"
    while True:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"Website loaded successfully at {current_time}.")
                break
            else:
                print(f"Unexpected status code: {response.status_code}. Retrying...")
        except requests.RequestException as e:
            print(f"Failed to load website: {e}. Retrying...")
        time.sleep(5)  # Wait 5 seconds before retrying

# Directly run the function
check_website()