from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PIL import Image
# from bs4 import BeautifulSoup
import requests
import os

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


def main():
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
    items = results.get('files', [])  # 所有圖片
    new_items = []  # 檔名＋ID
    if not items:
        print('No files found.')
    else:
        print('Files:')
        for item in items:
            new_items.append(u'{0}({1})'.format(item['name'][0:10], item['id']))
    photo = []  # 要找的照片的檔名+ID
    keyword_to_find = str('女秋＿白')  # 要找的照片的關鍵字:XX＿X，如：男秋＿白
    for a in new_items:
        if a.find(keyword_to_find) != -1:
            photo.append(a)
        else:
            continue
    # print(len(photo))  # 檢查是不是每個組合都是有照片的
    path = os.getcwd()  # 這個py檔的路徑，因為載下來的照片會存在這個py檔旁邊
    for i in range(0, len(photo)):  # 4張圖片
        url = 'https://drive.google.com/u/0/uc?id=' + photo[i][11:-1] + '&export=download'
        photo_sourse = requests.get(url)  # 讀網址檔
        with open('image.' + 'test' + str(i) + '.png', 'wb') as file:
            file.write(photo_sourse.content)
            img_in_screen = Image.open(path + '/image.test' + str(i) + '.png')
            # img_in_screen.show()
        os.remove(path=path + '/image.test' + str(i) + '.png')  # 移除載下的圖片

if __name__ == '__main__':
    main()
