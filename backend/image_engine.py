import openai
import json
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API")

def image_generation(image_prompt):
    # image_prompt = image_prompt + ",digital art, 4k, highly detailed, storybook"
    # response = openai.Image.create(
    # prompt= image_prompt,
    # n=1,
    # size="512x512"
    # )
    # image_url = response['data'][0]['url']

    image_url = "https://i.natgeofe.com/n/cfa19a0d-eff0-4628-8fdd-2ad8d66845dd/mountain-range-appenzell-switzerland_square.jpg"

    print(image_url)
    return image_url

