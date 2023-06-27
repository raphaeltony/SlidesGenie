from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from backend.connection import get_drive_service
from backend.connection import get_slides_service

#Connecting to the drive service
drive_service = get_drive_service()
slides_service = get_slides_service()


def create_title_slide(presentation_id, content,counter):
    requests = [
            {
                'replaceAllText': {
                    'containsText': {
                        'text': '<<title>>',
                        'matchCase': True
                    },
                    'replaceText': content['title'],
                    'pageObjectIds':[f'copiedSlide{counter}']
                }
            }
        ]

        # Execute the requests for this presentation.
    body = {
        'requests': requests
    }
    response = slides_service.presentations().batchUpdate(
        presentationId=presentation_id, body=body).execute()


def create_left_image_slide(presentation_id, content,counter):
    requests = [
            {
                'replaceAllText': {
                    'containsText': {
                        'text': '<<left-image-text_title>>',
                        'matchCase': True
                    },
                    'replaceText': content['title'],
                    'pageObjectIds':[f'copiedSlide{counter}']
                }
            },

            {
                'replaceAllText': {
                    'containsText': {
                        'text': '<<left-image-text_body>>',
                        'matchCase': True
                    },
                    'replaceText': content['body'],
                    'pageObjectIds':[f'copiedSlide{counter}']
                }
            },
    
            {
                'replaceAllShapesWithImage': {
                    'imageUrl': "https://images.nationalgeographic.org/image/upload/t_edhub_resource_key_image/v1638892314/EducationHub/photos/tennessee-power-plant.jpg",
                    'replaceMethod': 'CENTER_INSIDE',
                    'containsText': {
                        'text': '<<left-image-text_image>>',
                        'matchCase': True
                    },
                    'pageObjectIds':[f'copiedSlide{counter}']
                }
            }
    ]
    
    body = {
        'requests': requests
    }
    response = slides_service.presentations().batchUpdate(
        presentationId=presentation_id, body=body).execute()
    
def create_right_image_slide(presentation_id, content,counter):
    requests = [
            {
                'replaceAllText': {
                    'containsText': {
                        'text': '<<right-image-text_title>>',
                        'matchCase': True
                    },
                    'replaceText': content['title'],
                    'pageObjectIds':[f'copiedSlide{counter}']
                }
            },

            {
                'replaceAllText': {
                    'containsText': {
                        'text': '<<right-image-text_body>>',
                        'matchCase': True
                    },
                    'replaceText': content['body'],
                    'pageObjectIds':[f'copiedSlide{counter}']
                }
            },
    
            {
                'replaceAllShapesWithImage': {
                    'imageUrl': "https://images.nationalgeographic.org/image/upload/t_edhub_resource_key_image/v1638892314/EducationHub/photos/tennessee-power-plant.jpg",
                    'replaceMethod': 'CENTER_INSIDE',
                    'containsText': {
                        'text': '<<right-image-text_image>>',
                        'matchCase': True
                    },
                    'pageObjectIds':[f'copiedSlide{counter}']
                }
            }
    ]
    
    body = {
        'requests': requests
    }
    response = slides_service.presentations().batchUpdate(
        presentationId=presentation_id, body=body).execute()



def create_title_sub_text_slide(presentation_id, content,counter):
    requests = [
            {
                'replaceAllText': {
                    'containsText': {
                        'text': '<<title-sub-text_title>>',
                        'matchCase': True
                    },
                    'replaceText': content['title'],
                    'pageObjectIds':[f'copiedSlide{counter}']
                }
            },

            {
                     'replaceAllText': {
                    'containsText': {
                        'text': '<<title-sub-text_sub>>',
                        'matchCase': True
                    },
                    'replaceText': content['subtitle'],
                    'pageObjectIds':[f'copiedSlide{counter}']
                }
            },

            {
                'replaceAllText': {
                    'containsText': {
                        'text': '<<title-sub-text_body>>',
                        'matchCase': True
                    },
                    'replaceText': content['body'],
                    'pageObjectIds':[f'copiedSlide{counter}']
                }
            }
        ]

    # Execute the requests for this presentation.
    body = {
        'requests': requests
    }
    response = slides_service.presentations().batchUpdate(
        presentationId=presentation_id, body=body).execute()
