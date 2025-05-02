import requests
import random
import string

def generate_random_user():
    name = ''.join(random.choices(string.ascii_lowercase, k=8))
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
    return name, password

def create_temp_email():
    try:
        response = requests.get("https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1")
        email = response.json()[0]
        return email
    except Exception as e:
        return None

def create_temp_account():
    email = create_temp_email()
    username, password = generate_random_user()

    if not email:
        return {"status": "failed", "reason": "Email generation failed"}

    return {
        "email": email,
        "username": username,
        "password": password,
        "status": "success"
    }
