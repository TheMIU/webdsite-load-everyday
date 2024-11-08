import requests
import schedule
import time
from datetime import datetime

def check_website():
    url = "https://miusoft.info"  # Replace with your website URL
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

# Schedule the check_website function to run twice daily
schedule.every().day.at("00:00").do(check_website)  # Runs at midnight
schedule.every().day.at("12:00").do(check_website)  # Runs at noon
# schedule.every().minute.do(check_website) # to debug

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every minute if it's time to run the task
