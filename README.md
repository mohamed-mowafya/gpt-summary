# GPT Summary API
An API made with Flask that will take in a user's prompt in order to summarize articles using OpenAI's ChatGPT.

# How it works
Send a request to this endpoint: /prompt. You have to send a request with a json body in this format: 
```
{
    "message": "Summarize me this article: {URL}" (Without the brackets)
}
```
### IMPORTANT NOTE:
In order to not infringe copyright laws and rules, when using this API, make sure that the website containing the article that you are passing as an argument allows scraping.