import google.generativeai as genai
import os
from IPython.display import display
from IPython.display import Markdown
import pathlib
import textwrap



gemini_api_key = 'AIzaSyDAC1T59jvKl6qw4JJhyyco8Y6et_hQ8E4'
genai.configure(api_key = gemini_api_key)

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

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
The above JSON contains two slide templates: title, image-text. Use this to generate the slides for each keyword and nest the required details accurately. For each keyword, use the image-text slide and generate the response. RESPOND WITH JSON ONLY

'''

prompt3 = ''' content:

Features of a Monopoly Market 
Some characteristics of a monopoly market are as follows.

The product has only one seller in the market.

Monopolies possess information that is unknown to others in the market.

There are profit maximization and price discrimination associated with monopolistic markets. Monopolists are guided by the need to maximize profit either by expanding sales production or by raising the price.

It has high barriers to entry for any new firm that produces the same product.

The monopolist is the price maker, i.e., it decides the price, which maximizes its profit. The price is determined by evaluating the demand for the product.

The monopolist does not discriminate among customers and charges them all alike for the same product.

Some of the monopoly market examples are your local gas company, railways, Facebook, Google, Patents, etc.


'''

response = model.generate_content(prompt1 + prompt3)
print(response.text)
response = model.generate_content(prompt2 + response.text)
print(response.text)

# to_markdown(response.text)



def content_generation(user_input):
    user_input = "user input : "+ user_input

    response = model.generate_content(prompt1 + user_input)
    response = model.generate_content(prompt2 + response.text)
    print(response.text)



# print(response["choices"][0]["message"]["content"])

    d = json.loads(response["choices"][0]["message"]["content"]) 
    print(d)

    return d
  
