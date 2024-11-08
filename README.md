# Daily Website Availability Checker

This script checks if a specified website is available at two scheduled times each day (12:00 AM and 12:00 PM UTC) using GitHub Actions. If the website fails to load, it will keep retrying until successful.

## Features

- Checks website availability twice daily (12:00 AM and 12:00 PM UTC).
- Retries every 5 seconds if the website is unavailable.
- Logs a success message with a timestamp once the website loads successfully.
