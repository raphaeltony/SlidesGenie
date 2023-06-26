from flask import Flask

from backend.slides_manip import copy_presentation
from backend.slides_manip import get_presentation
from backend.slides_manip import create_slide_copy
from backend.slides_creation import create_title_slide,create_left_image_slide, create_title_sub_text_slide
app = Flask(__name__)

response = {'slides': 
            [{'type_id': 'title', 'inputs': {'title': 'Global Warming', 'subtitle': 'Understanding the Phenomenon'}}, {'type_id': 'left-image-text', 'inputs': {'title': 'Causes of Global Warming', 'image_prompt': 'A coal power plant emitting carbon dioxide', 'body': 'Global warming is primarily caused by the emission of greenhouse gases, such as carbon dioxide and methane, from human activities like burning fossil fuels and deforestation of forests'}}, {'type_id': 'right-image-text', 'inputs': {'title': 'Effects of Global Warming', 'image_prompt': 'A polar bear on melting ice', 'body': 'Climate change due to global warming is causing sea levels to rise, ice to melt, and weather patterns to change, which is leading to issues like stronger and more frequent natural disasters, displacement of people, and extinction of species.'}}, {'type_id': 'left-image-text', 'inputs': {'title': 'Impact on Oceans', 'image_prompt': 'Coral reefs dying due to ocean acidification', 'body': 'Global warming is causing oceans to warm up and become more acidic, which is leading to coral bleaching, loss of marine life, anglobal warming by reducing their carbon footprint, adopting sustainable business practices, and investing in clean technologies. Doing so not only benefits the environment, but can also improve bottom lines and help companies stay competitive in a rapidly changing world.'}}, {'type_id': 'title-sub-text', 'inputs': {'title': 'The Urgency of Action', 'subtitle': 'Why We Must Act Now', 'body': 'Global warming is one of the greatest threats facing humanity and the planet. Failure to act now will lead to irreparable damage to the environment, social and economic disruptions, and loss of life. It is up to each and every individual to do their part in addressing this global crisis.'}}]}


@app.route("/")
def hello_world():
    return "<p>Hello, people</p>"

@app.route("/submit")
def process_input():
    
    new_presentation_id = copy_presentation("1Qw0oqIpGSrEyQZkFhFnzxj6-4kMq8X1TnSdqpG94Ch8",response['slides'][0]['inputs']['title'])
    new_slides = get_presentation(new_presentation_id)

    counter = 0
    
    for slide in response['slides']:
        create_slide_copy(new_presentation_id,new_slides,slide['type_id'],counter)

        if(slide['type_id'] == 'title'):
            create_title_slide(new_presentation_id,slide['inputs'],counter)

        elif(slide['type_id'] == 'left-image-text'):
            create_left_image_slide(new_presentation_id,slide['inputs'], counter)

        # elif(slide['type_id'] == 'right-image-text'):
        #     create_right_image(new_presentation_id,slide['inputs'], counter)

        elif(slide['type_id'] == 'title-sub-text'):
            create_title_sub_text_slide(new_presentation_id,slide['inputs'], counter)

        counter = counter + 1
    return "Presentation created succesfully"



