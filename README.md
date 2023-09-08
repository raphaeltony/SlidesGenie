# Memory Lane and Slides Genie

This project has two components:
- **Memory Lane**: An AI-powered learning tool that creates bizarre stories around the input learning material and presents it in a visual format to improve retention.
- **SlideGenie**: An AI slides generator that generates Google Slides presentations based on the topic entered by the user.

https://github.com/raphaeltony/SlidesGenie/assets/30729856/484800ea-040f-4e01-801a-1ee8db7b2249


## Memory Lane Component (AI Learning Tool)

__Memory Lane__ is a learning tool to enhance memory retention. Users can input learning materials. The application identifies the keywords and automatically generates interconnected vivid imagery. These visual associations can be easily memorized and running through the visuals in your mind easily helps in recalling the keywords. This improves memory retention, making learning engaging and memorable. This is achieved with ChatGPT, DALL-E, and Google Slides.

## SlidesGenie (AI Slides Generation)

The __SlidesGenie__ component allows users to input a topic. ChatGPT API is used to generate the presentation content and DALL-E API is used for generating the visuals. These are then integrated and saved to Google Slides.


![interaction diagram](/docs/diagram.jpg)

## Pre-requisites
- Python
- All dependencies mentioned in `requirements.txt`
- A Google Cloud Platform project with the **Drive API** and **Google Slides API** enabled, along with its authorization credentials for a desktop application. Check out the following section [(Setting Up Google Cloud Console)](#setting-up-google-cloud-console) to learn how to implement this.
- OpenAI API Key: Create a .env file and save the contents with `OPENAI_API=<your-key-here>`

## Setting Up Google Cloud Console

- To create presentations on the user's account, a Google Cloud Platform project must be set up with the **_Drive API_** and **_Google Slides API_** enabled. Then the user credentials must be downloaded and placed in the same folder as the script.

- Follow the steps mentioned in this [link](https://developers.google.com/slides/api/quickstart/python) 

> After downloading the file, rename it to 'credentials' and place it in the same folder as the project

## Running the Script
- The project is built on Flask and can be run with the command :
```
python -m flask --app main.py run
```
