from __future__ import print_function

from googleapiclient.errors import HttpError
from backend.connection import get_drive_service
from backend.connection import get_slides_service

#Connecting to the drive service
drive_service = get_drive_service()
slides_service = get_slides_service()

def copy_presentation(presentation_id, copy_title):
    """
           Creates the copy Presentation the user has access to.
           Load pre-authorized user credentials from the environment.
           TODO(developer) - See https://developers.google.com/identity
           for guides on implementing OAuth2 for the application.
           """
    try:
        body = {
            'name': copy_title
        }
        drive_response = drive_service.files().copy(
            fileId=presentation_id, body=body).execute()
        presentation_copy_id = drive_response.get('id')

    except HttpError as error:
        print(f"An error occurred: {error}")
        print("Presentations  not copied")
        return error

    return presentation_copy_id

# new_id = copy_presentation("1Qw0oqIpGSrEyQZkFhFnzxj6-4kMq8X1TnSdqpG94Ch8","My presentation")
# print(new_id)

def create_slide_copy(presentation_id,slides,slide_type,counter):
    if slide_type == 'title':
        pageId = slides[0]['objectId']
    elif slide_type == 'left-image-text':
        pageId = slides[1]['objectId']
    elif slide_type == 'right-image-text':
        pageId = slides[2]['objectId']
    elif slide_type == 'title-sub-text':
        pageId = slides[3]['objectId']

    #for memorylane
    elif slide_type == 'image-text':
        pageId = slides[1]['objectId']

    requests = {
    "requests" : [
    {
      "duplicateObject": {
        "objectId": pageId,
        "objectIds": {
          pageId: "copiedSlide" + str(counter),
        }
      }
    }
    ]
    }

    try:
        response = slides_service.presentations() \
            .batchUpdate(presentationId=presentation_id, body=requests).execute()

    except HttpError as error:
        print(f"An error occurred: {error}")
        print("Slide not copied")
        return error
    

def get_presentation(presentation_id):
    presentation = slides_service.presentations().get(presentationId=presentation_id).execute()
    slides = presentation.get('slides')
    print(slides)
    return slides


