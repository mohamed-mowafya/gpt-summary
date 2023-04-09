import os
import openai
import re
from helpers import web_scraper_helper
import validators
from enums.prompt_type import PromptType

def _get_url(message):
    """
    Function that extracts a url from a message, using regex.
    """
    regex = "(?P<non_url>.*?)(?P<url>https?://[^\s]+)"

    match = re.search(regex, message)
    url_text = ""
    non_url_text = ""

    if match:
        non_url_text = match.group("non_url").strip()
        url_text = match.group("url").strip()
    
    return url_text, non_url_text

def _is_google_search(message):
    pass


def prompt(json_obj):
    API_SECRET = os.getenv('OPEN_AI_SECRET')
    openai.api_key = API_SECRET
    possible_url, non_url_text = _get_url(json_obj["message"])
    user_content = non_url_text

    if validators.url(possible_url):
        user_content += web_scraper_helper.get_content(possible_url)
    
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": PromptType.GPT_PROMPT.value},
        {"role": "user", "content": user_content}
    ]
)

    return completion

