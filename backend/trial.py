import re
text = '''
```
{
  "slides": [
    {
      "type_id": "title",
      "inputs": {
        "title": "Monopoly Market"
      }
    },
    {
      "type_id": "image-text",
      "inputs": {
        "keyword": "Single seller",
        "visual": "A giant, solitary tree standing alone in a field, its roots firmly planted."
      }
    },
    {
      "type_id": "image-text",
      "inputs": {
        "keyword": "Exclusive information",
        "visual": "The tree whispering secrets to the wind, making it sway."
      }
    },
    {
      "type_id": "image-text",
      "inputs": {
        "keyword": "Profit maximization and price discrimination",
        "visual": "Leafy moneybags hanging from the tree's branches, while the wind blows them around."
      }
    },
    {
      "type_id": "image-text",
      "inputs": {
        "keyword": "High barriers to entry",
        "visual": "Thorny vines wrapped around the tree's trunk, preventing others from climbing."
      }
    },
    {
      "type_id": "image-text",
      "inputs": {
        "keyword": "Price maker",
        "visual": "A crown perched atop the tree, its shape determined by the wind's direction."
      }
    },
    {
      "type_id": "image-text",
      "inputs": {
        "keyword": "No price discrimination",
        "visual": "Identical figurines scattered around the tree, all the same size and shape."
      }
    },
    {
      "type_id": "image-text",
      "inputs": {
        "keyword": "Examples",
        "visual": "The tree's shadow stretching across the field, reaching towards a nearby city where skyscrapers representing Facebook, Google, and other monopolies rise high."
      }
    }
  ]
}
```
'''

json_content = re.search(r'\{.*\}', text, re.DOTALL).group(0)

print(json_content)