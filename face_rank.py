from aip import AipFace
import base64
from imutils import paths
import cv2
import re

APP_ID = '19919038'
API_KEY = '2WC88q9VuzeWR8pIBmf3yHMn'
SECRET_KEY = 'bYdUvDeut8c9teaCXL1zCkZpWjLriG1G'

aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

filePath = './image/'
res_path = './Result/'
def get_file_content(filePath):
       with open(filePath, 'rb') as fp:
              content = base64.b64encode(fp.read())
              return content.decode('utf-8')

imageType = "BASE64"

options = {}
options["face_field"] = "age,gender,beauty"
res = {}
for index,i in enumerate(paths.list_images("./image")):
       print("[INFO] Processing {} image".format(index+1))
       with open(i, 'rb') as fp:
              content = base64.b64encode(fp.read())
              mark = aipFace.detect(content.decode('utf-8'),imageType,options)["result"]['face_list'][-1]["beauty"]
       res[i] = mark
r = sorted(res.items(), key=lambda kv: (-kv[1], kv[0]))
for tup in r:
       i,j = tup
       img = cv2.imread(i)
       n = re.sub("\D", "", i)
       img_name = res_path +str(j)+"_"+n+'.png'
       cv2.imwrite(img_name, img)
       print("[RESULT] Mark {} image {}".format(j,n))
print("[FINISH]")
