from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import sys

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
drive = GoogleDrive(gauth)

try:
    name = '韓系男友風＿夏＿藍色.png'  # It's the file which you'll upload
    file = drive.CreateFile()  # Create GoogleDriveFile instance
    file.SetContentFile(name)
    file.download()
except :
    print("Unexpected error:", sys.exc_info()[0])