import google.generativeai as genai
import os
# from IPython.display import display
# from IPython.display import Markdown
# import pathlib
# import textwrap
import json
import re
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key = os.getenv("GEMINI_API"))

# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

model = genai.GenerativeModel('gemini-pro')


prompt1 ='''You are an AI called MemoryLane. You help people to remember study material by using mnemonic images that use vivid strange imagery.  Consider the following user input.
Identify the main topic and generate short keywords related to that topic from the input. 
Generate vivid imagery for each of the keywords in such a way that each imagery connects to the next keyword's imagery.
Make sure that each imagery connects to the next keyword's imagery.
'''

prompt2 = '''
You have to convert the content as a slides presentation. Create the structure of the slides presentation as a JSON object.
You have 2 slide formats. Each slide has a type_id and takes different inputs. The slide formats are:
1. Title Slide
The title slide consists of a title and a subtitle.
type_id:title
inputs: title
2. Slide with visual description
The slide consists of the keyword and the visual description.
type_id: image-text
inputs: keyword, visual.
Template:
```
{
  "slides": [
    {
      "type_id": "title",
      "inputs": {
        "title": "<insert-title>"
      }
    },
    {
      "type_id": "image-text",
      "inputs": {
        "keyword": "<insert-keyword>",
        "visual": "<insert-keyword-visual-description>"
      }
    },

  ]
}

```
The above JSON contains two slide templates: title, image-text. Use this to generate the slides for each keyword and nest the required details accurately. For each keyword, use the image-text slide and generate the response. 
RESPOND WITH JSON ONLY. No other text is needed
'''

def gemni_visualize(user_input):
  user_input = "user input : "+ user_input

  response = model.generate_content(prompt1 + user_input)
  response = model.generate_content(prompt2 + response.text)
  json_content = re.search(r'\{.*\}', response.text, re.DOTALL).group(0)
  d = json.loads(json_content) 
  print("USING GEMINI")
  print(d)

  return d
  
