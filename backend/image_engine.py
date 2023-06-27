import openai
import json

def image_generation():
    response = openai.Image.create(
    prompt="a white siamese cat",
    n=1,
    size="1024x1024"
    )
    image_url = response['data'][0]['url']

print(image_url)