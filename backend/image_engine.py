from openai import OpenAI, RateLimitError
import json
from dotenv import load_dotenv
import os
from time import sleep

load_dotenv()

def image_generation(image_prompt):
    client = OpenAI(api_key=os.getenv("OPENAI_API"))

    image_prompt = image_prompt + ",digital art, 4k, highly detailed, storybook"
    
    for i in range(6):
        try:
            response = client.images.generate(
                model="dall-e-2",
                prompt = image_prompt,
                n=1,
                size="512x512"
            )

            image_url = response.data[0].url
            # image_url = "https://i.natgeofe.com/n/cfa19a0d-eff0-4628-8fdd-2ad8d66845dd/mountain-range-appenzell-switzerland_square.jpg"
            print(image_url)
            return image_url
        
        except RateLimitError:
            print("Rate limit exceeded, retrying in 30 secs")
            sleep(30)
            continue
        except Exception as e:
            print(e)

    return ""




    

