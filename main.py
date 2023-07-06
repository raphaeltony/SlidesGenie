from flask import Flask

from backend.slides_manip import copy_presentation
from backend.slides_manip import get_presentation
from backend.slides_manip import create_slide_copy
from backend.GPT_engine import content_generation
from backend.memory_lane import visualize
from backend.slides_creation import create_title_slide,create_left_image_slide,create_right_image_slide, create_title_sub_text_slide,create_image_slide
app = Flask(__name__)

# response = {'slides': 
            # [{'type_id': 'title', 'inputs': {'title': 'Global Warming', 'subtitle': 'Understanding the Phenomenon'}}, {'type_id': 'left-image-text', 'inputs': {'title': 'Causes of Global Warming', 'image_prompt': 'A coal power plant emitting carbon dioxide', 'body': 'Global warming is primarily caused by the emission of greenhouse gases, such as carbon dioxide and methane, from human activities like burning fossil fuels and deforestation of forests'}}, {'type_id': 'right-image-text', 'inputs': {'title': 'Effects of Global Warming', 'image_prompt': 'A polar bear on melting ice', 'body': 'Climate change due to global warming is causing sea levels to rise, ice to melt, and weather patterns to change, which is leading to issues like stronger and more frequent natural disasters, displacement of people, and extinction of species.'}}, {'type_id': 'left-image-text', 'inputs': {'title': 'Impact on Oceans', 'image_prompt': 'Coral reefs dying due to ocean acidification', 'body': 'Global warming is causing oceans to warm up and become more acidic, which is leading to coral bleaching, loss of marine life, anglobal warming by reducing their carbon footprint, adopting sustainable business practices, and investing in clean technologies. Doing so not only benefits the environment, but can also improve bottom lines and help companies stay competitive in a rapidly changing world.'}}, {'type_id': 'title-sub-text', 'inputs': {'title': 'The Urgency of Action', 'subtitle': 'Why We Must Act Now', 'body': 'Global warming is one of the greatest threats facing humanity and the planet. Failure to act now will lead to irreparable damage to the environment, social and economic disruptions, and loss of life. It is up to each and every individual to do their part in addressing this global crisis.'}}]}

response = {'slides': [{'type_id': 'title', 'inputs': {'title': 'Features of a Monopoly Market'}}, {'type_id': 'image-text', 'inputs': {'keyword': 'Monopoly Market', 'visual': 'Imagine a bustling marketplace, but with a single vendor standing alone in the center, surrounded by empty stalls. The market is dominated by this solitary figure.'}}, {'type_id': 'image-text', 'inputs': {'keyword': 'One Seller', 'visual': "Visualize this seller as \
a giant towering over the rest of the market, holding a sign that reads 'Only I can sell!' The other vendors cower in fear and submission."}}, {'type_id': 'image-text', 'inputs': {'keyword': 'Unknown Information', 'visual': 'Picture the monopolist wearing a cloak of shadows, whispering secrets to themselves. They hold hidden knowledge that gives them a mysterious advantage over the others.'}}, {'type_id': 'image-text', 'inputs': {'keyword': 'Profit Maximization', 'visual': 'See the monopolist transforming into a money-hungry monster, with coins spouting from their greedy mouth. They have an insatiable desire for wealth and are willing to devour everything in their path to achieve maximum profit.'}}, {'type_id': 'image-text', 'inputs': {'keyword': 'Price Discrimination', 'visual': 'Imagine the monopolist wearing a hat with different colored bands. Each \
band represents a different price level, symbolizing how they extract more money from customers based on their willingness or ability to pay.'}}, {'type_id': 'image-text', 'inputs': {'keyword': 'High Barriers to Entry', 'visual': 'Envision a large impenetrable wall surrounding the market, guarded by dragons and mountains. It seems impossible for any new firm to enter and compete with the monopolist.'}}, {'type_id': 'image-text', 'inputs': {'keyword': 'Price Maker', 'visual': 'Picture the monopolist holding a giant gavel, ready to hammer down the price of the product. They possess the ultimate power to dictate the value of their goods, transcending any interference from the market or competitors.'}}, {'type_id': 'image-text', 'inputs': {'keyword': 'Demand', 'visual': "See a crowd of people, each holding a sign representing their desire for the monopolist's product. The monopolist uses a magnifying glass to selectively analyze each person's demand, measuring their willingness to pay and determining the price accordingly."}}, {'type_id': 'image-text', 'inputs': {'keyword': 'No Discrimination', 'visual': 'Imagine the monopolist standing on a stage, surrounded by a diverse audience of individuals. The monopolist wears a blindfold, representing their refusal to differentiate between customers based on any factors. All customers are treated equally, paying the same price for the same product.'}}]} 



@app.route("/")
def hello_world():
    return "<p>Hello, people</p>"

@app.route("/memorylane")
def memory():
    # response = visualize(user_input)

    new_presentation_id = copy_presentation("1oBjYbkCRWQwhOiNC4hHTMsuwIaURzPQvpYjXm2QVYLM",response['slides'][0]['inputs']['title'])
    new_slides = get_presentation(new_presentation_id)
    
    counter = 0

    for slide in response['slides']:
        create_slide_copy(new_presentation_id,new_slides,slide['type_id'],counter)

        if(slide['type_id'] == 'title'):
            create_title_slide(new_presentation_id,slide['inputs'],counter)

        elif(slide['type_id'] == 'image-text'):
            create_image_slide(new_presentation_id,slide['inputs'], counter)

        counter = counter + 1
    return "Presentation created succesfully"



@app.route("/submit")
def process_input():

    response = content_generation(user_input)


    new_presentation_id = copy_presentation("1Qw0oqIpGSrEyQZkFhFnzxj6-4kMq8X1TnSdqpG94Ch8",response['slides'][0]['inputs']['title'])
    new_slides = get_presentation(new_presentation_id)

    counter = 0
    
    for slide in response['slides']:
        create_slide_copy(new_presentation_id,new_slides,slide['type_id'],counter)

        if(slide['type_id'] == 'title'):
            create_title_slide(new_presentation_id,slide['inputs'],counter)

        elif(slide['type_id'] == 'left-image-text'):
            create_left_image_slide(new_presentation_id,slide['inputs'], counter)

        elif(slide['type_id'] == 'right-image-text'):
            create_right_image_slide(new_presentation_id,slide['inputs'], counter)

        elif(slide['type_id'] == 'title-sub-text'):
            create_title_sub_text_slide(new_presentation_id,slide['inputs'], counter)

        counter = counter + 1
    return "Presentation created succesfully"




