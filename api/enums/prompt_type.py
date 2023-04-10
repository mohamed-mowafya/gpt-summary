from enum import Enum


class PromptType(Enum):
    GPT_PROMPT = "You're a kind helpful assistant who can summarize articles that he will receive, when asked. If you don't have real time access to the information asked and the prompt does not provide a url. In any other case, just reply as a helpful AI bot."
    REAL_TIME_ACCESS_ACT = "Act like you can access the articles in real-time."