from __future__ import print_function

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from backend.connection import get_drive_service
from backend.connection import get_slides_service

#Connecting to the drive service
drive_service = get_drive_service()
slides_service = get_slides_service()