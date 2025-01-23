import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def search_update_links(json_file_path):
    # Load the JSON file
    with open(json_file_path, 'r') as file:
        bars = json.load(file)

    # Init Selenium WebDriver
    driver = webdriver.Chrome()  # ensure 'chromedriver' in PATH

    try:
        for bar in bars:
            bar_name = bar.get("Name")
            current_url = bar.get("URL", "")

            # Skip if URL already exists
            if current_url and current_url.startswith("http"):
                print(f"URL for '{bar_name}' already exists. Skipping...")
                continue

            # Search on Google
            search_query = f"{bar_name} NYC official site"
            driver.get("https://www.google.com")
            search_box = driver.find_element(By.NAME, "q")
            search_box.send_keys(search_query)
            search_box.send_keys(Keys.RETURN)

            time.sleep(3) # wait for results to load

            # Get first result URL
            try:
                first_result = driver.find_element(By.CSS_SELECTOR, "div.yuRUbf a")
                bar_url = first_result.get_attribute("href")
                print(f"Found URL for '{bar_name}': {bar_url}")
                bar["URL"] = bar_url  # Update the JSON data
            except Exception as e:
                print(f"Could not find URL for '{bar_name}'. Error: {e}")
                continue

    finally: driver.quit() # close browser

    # Save updated JSON back to file
    with open(json_file_path, 'w') as file:
        json.dump(bars, file, indent=4)

    print("JSON file updated with URLs.")