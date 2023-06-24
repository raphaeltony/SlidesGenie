from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from backend.connection import get_drive_service
from backend.connection import get_slides_service

#Connecting to the drive service
drive_service = get_drive_service()
slides_service = get_slides_service()


def create_title_slide(presentaion_id, content):
    requests = [
            {
                'replaceAllText': {
                    'containsText': {
                        'text': '<<title>>',
                        'matchCase': True
                    },
                    'replaceText': content['title']
                }
            }
        ]

        # Execute the requests for this presentation.
    body = {
        'requests': requests
    }
    response = slides_service.presentations().batchUpdate(
        presentationId=presentaion_id, body=body).execute()
