from openai import OpenAI
import json
import re
from dotenv import load_dotenv
import os
from backend.prompt_examples import user_inputs,assistant_answers
load_dotenv()

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
The above JSON contains two slide templates: title, image-text. Use this to generate the slides for each keyword and nest the required details accurately. For each keyword, use the image-text slide and generate the response. RESPOND WITH JSON ONLY

'''


def visualize(user_input,llm):  
    gpt_model = ''
    example_messages = []


    if(llm == '1'):
      gpt_model = 'gpt-3.5-turbo'
      example_messages=[
                {"role": "system", "content": prompt1},
                {"role": "user", "content": user_inputs[0]},
                {"role": "assistant", "content": assistant_answers[0]},
                {"role": "user", "content": user_inputs[1]},
                {"role": "assistant", "content": assistant_answers[1]},
                {"role": "user", "content": user_inputs[2]},
                {"role": "assistant", "content": assistant_answers[2]},
                {"role": "user", "content": user_input},
            ]
    else:
      gpt_model = 'gpt-4-0125-preview'
      example_messages=[
                {"role": "system", "content": prompt1},
                {"role": "user", "content": user_input},
            ]
    
    user_input = "user input : "+ user_input

    client = OpenAI(api_key=os.getenv("OPENAI_API"))

    response = client.chat.completions.create(
      model=gpt_model,
      messages=example_messages
    )
    content = "content: "+ str(response.choices[0].message.content)
    print("USING ", gpt_model)
    print(content)


    # gpt-4-0125-preview
    response = client.chat.completions.create(
      model=gpt_model,
      messages=[
                {"role": "system", "content": prompt2},
                {"role": "user", "content": content},
            ]
    )
    print(response.choices[0].message.content)

    json_content = re.search(r'\{.*\}', response.choices[0].message.content, re.DOTALL).group(0)
    d = json.loads(json_content) 
    print(d)

    return d

