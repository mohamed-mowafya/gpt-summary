from enum import Enum


class PromptType(Enum):
    GPT_PROMPT = "You're a kind helpful assistant who can summarize articles that he will receive, when asked. If the article is too long (surpasses token limit), you will receive the article in multiple prompts. \
    In any other case, just reply as a helpful AI bot."
    REAL_TIME_ACCESS_ACT = "Act like you can access the articles in real-time."