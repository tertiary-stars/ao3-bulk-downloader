import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

def login(): # So I can change the login method later on
    # Load credentials
    load_dotenv()
    USERNAME = os.getenv("AO3_USERNAME")
    PASSWORD = os.getenv("AO3_PASSWORD")

    if not USERNAME or not PASSWORD:
        raise ValueError("Missing AO3 credentials in .env file.")

    # Use these credentials for the login logic
    print(f"Logging in as {USERNAME}")
    # (Add your login logic here, e.g., using `requests` or `selenium`)

    return USERNAME, PASSWORD

# Initialize session
session = requests.Session()

USERNAME, PASSWORD = login()

# Get the login page to extract CSRF token
login_url = "https://archiveofourown.org/users/login"
login_page = session.get(login_url)
soup = BeautifulSoup(login_page.text, "html.parser")

# Extract CSRF token
csrf_token = soup.find("input", {"name": "authenticity_token"})["value"]

# Send login request
payload = {
    "user[login]": USERNAME,
    "user[password]": PASSWORD,
    "authenticity_token": csrf_token,
    "commit": "Log in",
}

response = session.post(login_url, data=payload)

# Verify login success
if "Successfully logged in" in response.text or f"Hi, {USERNAME}" in response.text:
    print("Login successful!")
    login = True
elif "user_session" in session.cookies.get_dict():
    print("Login successful (via session cookie)!")
    login = True
else:
    print("Login failed!")
    login = False

# Debug: Save response to inspect in a browser if needed
with open("response.html", "w", encoding="utf-8") as file:
    file.write(response.text)


if login:
    # Fetch user's works
    works_url = f"https://archiveofourown.org/users/{USERNAME}/works"
    works_page = session.get(works_url)
    soup = BeautifulSoup(works_page.text, 'html.parser')

    # Scrape story titles and links
    stories = soup.find_all("li", class_="work")
    story_list = {}
    for i, story in enumerate(stories):
        title = story.find("a").text
        link = "https://archiveofourown.org" + story.find("a")["href"]
        story_list[i + 1] = {"title": title, "link": link}
        print(f"{i + 1}. {title}")

    # Allow user to select a story
    choice = int(input("Select a story by number: "))
    selected_story = story_list[choice]
    print(f"Selected story: {selected_story['title']} ({selected_story['link']})")

else:
    print("Login failed!")


