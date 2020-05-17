import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time

url = "https://www.nogizaka46-cn.com/nogizaka-member/index"
fie = "https://www.nogizaka46-cn.com"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers) 
soup = BeautifulSoup(response.content, 'html.parser')
items = soup.findAll(class_='thumbnail')
folder_path = './image/'
if os.path.exists(folder_path) == False:  
    os.makedirs(folder_path)  
 
for index,item in enumerate(items):
	if item:
		# print(item.get('src'))
		# html = fie + item.get('src')		
		html = requests.get(fie + item.get('src')) 
		
		img_name = folder_path + str(index + 1) +'.png'
		with open(img_name, 'wb') as file: 
			file.write(html.content)
			file.flush()
		file.close()  
		print('[INFO] Prossing %d image' %(index+1))
print('[FINISH]')