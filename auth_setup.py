import json
import requests
from bs4 import BeautifulSoup

def ao3_login():
    # Load credentials
    with open("config.json") as config_file:
        config = json.load(config_file)
        username = config["credentials"]["AO3_USERNAME"]
        password = config["credentials"]["AO3_PASSWORD"]

    # Start a session
    session = requests.Session()
    login_url = "https://archiveofourown.org/users/login"
    login_page = session.get(login_url)
    soup = BeautifulSoup(login_page.text, "html.parser")

    # Extract CSRF token
    csrf_token = soup.find("input", {"name": "authenticity_token"})["value"]

    # Prepare login payload
    payload = {
        "user[login]": username,
        "user[password]": password,
        "authenticity_token": csrf_token,
        "commit": "Log in"
    }

    # Perform login
    response = session.post(login_url, data=payload)

    # Verify login success
    if "Successfully logged in" in response.text or f"Hi, {username}" in response.text:
        print("Login successful!")
        return session
    elif "user_session" in session.cookies.get_dict():
        print("Login successful (via session cookie)!")
        return session
    else:
        print("Login failed!")

    


if __name__ == "__main__":
    session = ao3_login()
    if session:
        with open("ao3_session.json", "w") as session_file:
            json.dump(session.cookies.get_dict(), session_file)
