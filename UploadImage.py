import cv2
import dropbox
import time
import random


start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name

    videoCaptureObject.release()

    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token="sl.A3ZXSyVHR7040ldyIh6oH30E253Lt-UKmvy_EFxKebCAXsKiWADuGY_-zjIiZLMMBacTJy5fnTWlECDOjKcv4tpFI_a_QW82dWNVn1juDqVes43EmjXsaefcPHyB--wpj-N55es"
    file=img_name
    file_from=file
    file_to="/newfolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("Files Uploaded")
def main():
    while(True):
        if((time.time()-start_time)>=30):
            name=take_snapshot()
            upload_file(name)
main()

    