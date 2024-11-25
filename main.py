import requests
from bs4 import BeautifulSoup

# AO3 credentials
USERNAME = "your_username"
PASSWORD = "your_password"

# Initialize session
session = requests.Session()

# Login
login_url = "https://archiveofourown.org/users/login"
payload = {
    "user[login]": USERNAME,
    "user[password]": PASSWORD,
    "commit": "Log in"
}

response = session.post(login_url, data=payload)

if "Logout" in response.text:
    print("Logged in successfully!")

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
