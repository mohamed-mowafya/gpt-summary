import os
import openai
import re
from helpers import web_scraper_helper
import validators
from enums.prompt_type import PromptType

MESSAGES = [{"role": "system", "content": PromptType.GPT_PROMPT.value}]
GPT_PROMPT_LIMIT = 4097

def _get_url(message):
    """
    Function that extracts a url from a message, using regex.
    """
    regex = "(?P<non_url>.*?)(?P<url>https?://[^\s]+)"

    match = re.search(regex, message)
    url_text = ""
    non_url_text = message

    if match:
        non_url_text = match.group("non_url").strip()
        url_text = match.group("url").strip()
    
    return url_text, non_url_text

def _ask_gpt():
    """
    Function that will send a prompt to gpt.
    """
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=MESSAGES
    )
    return completion

def prompt(json_obj):
    """
    Main helper function that takes care of the logic, depending on user input.
    """
    API_SECRET = os.getenv('OPEN_AI_SECRET')
    openai.api_key = API_SECRET
    possible_url, non_url_text = _get_url(json_obj["message"])
    user_content = non_url_text

    if validators.url(possible_url):
        web_content = web_scraper_helper.get_content(possible_url)
        if len(web_content) > GPT_PROMPT_LIMIT:
            web_content = web_content[:GPT_PROMPT_LIMIT - len(user_content)]

        user_content+= web_content

    MESSAGES.append({"role": "user", "content": user_content})
    
    completion = _ask_gpt()

    return completion

