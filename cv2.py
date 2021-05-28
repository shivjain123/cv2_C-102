import cv2
import dropbox
import time
import random

start_time = time.time()

def takePicture():
    number = random.randint(1,100)
    videoObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoObject.read()
        print(ret)
        imageName = "Image" + str(number) + ".jpg"
        cv2.imwrite(imageName, frame)
        #start_time = time.time()
        result = False
    
    videoObject.release()
    cv2.destroyAllWindows()
    print("Your picture has been captured.")
    return imageName

def upload_files(imageName):
    access_token = "ksAyx1HqRZ4AAAAAAAAAAXenJVA7FF-0W9et3dBwy9FIOM5mwgoJsck9jU212snd"
    dbx = dropbox.Dropbox(access_token)
    file_from = imageName
    file_to = '/image/'

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to)
        print("Your file has been uploaded.")

def main():
    while(True):
        if((time.time() - start_time) > 5):
            name = takePicture()
            upload_files(name)

main()
