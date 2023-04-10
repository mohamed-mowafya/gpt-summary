from flask import request
from helpers import prompt_helper

def prompt():
    json_obj = request.json

    if 'message' not in json_obj:
        return {"status": "Missing parameters."}
    
    return prompt_helper.prompt(json_obj)