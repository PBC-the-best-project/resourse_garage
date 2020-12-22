from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PIL import Image
from bs4 import BeautifulSoup
import requests
import os

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


def main():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret_file.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Call the Drive v3 API
    results = service.files().list(
        pageSize=288, fields="nextPageToken, files(id, name)").execute()
    items = results.get('files', [])
    new_items = []
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in range(0, len(items)):
            new_items.append(u'{0}({1})'.format(items[item]['name'][0:10], items[item]['id']))
    photo = []
    for a in new_items:
        if a.find('秋＿白') != -1:
            photo.append(a)
        else:
            continue
    print(photo)
    path = os.getcwd()
    for i in range(0, 4):
        url = 'https://drive.google.com/u/0/uc?id=' + photo[i][11:-1] + '&export=download'
        photo_sourse = requests.get(url)
        with open('image.' + 'test' + str(i) + '.png', 'wb') as file:
            file.write(photo_sourse.content)
            an = Image.open(path + '/image.test' + str(i) + '.png')
        os.remove(path=path + '/image.test' + str(i) + '.png')

if __name__ == '__main__':
    main()
