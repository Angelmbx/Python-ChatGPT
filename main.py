# first step: pip install openai

from openai import OpenAI
import config

client = OpenAI(
    # api_key = config.api_key # openai api key configuration
)

content = input("Hi there, what do you wanna learn today? ") # saves whatever you type here in the variable 'content', that will be sent later in 'response' to the openai API

# "This allows you to provide context to the system, so that the responses will be slightly more oriented towards a specific domain or based on what you have written in the content."
'''
messages = [{"role": "system", "content": "You are an English-to-Spanish translation assistant."}]
'''

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": content}])

print(response.choices[0].message.content)
