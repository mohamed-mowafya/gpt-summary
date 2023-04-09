import os
import openai
from helpers import web_scraper_helper
import validators

def prompt(json_obj):
    API_SECRET = os.getenv('OPEN_AI_SECRET')
    openai.api_key = API_SECRET
    user_content = json_obj["message"]

    if validators.url(json_obj["message"]):
        user_content = web_scraper_helper.get_content(json_obj["message"])
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You're a kind helpful assistant who will summarize articles that he will receive."},
        {"role": "user", "content": user_content}
    ]
)

    return completion

