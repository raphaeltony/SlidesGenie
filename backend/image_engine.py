import openai
import json
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API")

def image_generation(image_prompt):

    response = openai.Image.create(
    prompt= image_prompt,
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']

    print(image_url)
    return image_url