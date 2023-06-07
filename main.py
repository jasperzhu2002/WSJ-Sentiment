import os
import openai
from scraper import getData
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPEN_AI_KEY')
openai.api_base = os.getenv('OPEN_AI_ENDPOINT')
openai.api_type = 'azure'
openai.api_version = '2023-03-15-preview' 

# gets the chat gpt reponse
def get_completion(prompt, deployment_name='gpt35'):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message.content

# scrapes for news
data = getData("nvidia")
headlines = data[0]
blurbs = data[1]
# compiles all the sentiments into a score 0 - 1
positive = 0
negative = 0
neutral = 0
# looks at headlines
for i in range(len(headlines)):
    prompt = f"""
    What is the sentiment of the following news headline, 
    which is delimited with triple backticks? Please respond
    exactly one word: positive, neutral, or negative.

    Review text: '''{headlines[i]}'''
    """
    response = get_completion(prompt)
    print(headlines[i])
    # checks for response
    if response == "positive":
        positive += 1
    elif response == "negative":
        negative += 1
    else:
        neutral += 1
# looks at blurbs
for i in range(len(blurbs)):
    prompt = f"""``
    What is the sentiment of the following news article blurb, 
    which is delimited with triple backticks? Please respond
    exactly one word: positive, neutral, or negative.

    Review text: '''{blurbs[i]}'''
    """
    response = get_completion(prompt)
    print(blurbs[i])
    # checks for response
    if response == "positive":
        positive += 1
    elif response == "negative":
        negative += 1
    else:
        neutral += 1

print(f"Positive count: {positive}, Neutral count: {neutral}, Negative count: {negative},")