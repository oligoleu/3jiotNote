from bs4 import BeautifulSoup as bs
import requests as rs

headers = {'Content-Type':'application/x-www-form-urlencoded'}
content = 'generalno=16014&version=zh_TW&pageNum=5&pages=139'
r = rs.post('https://www.cnsonline.com.tw/preview/GetData', data=content, headers=headers, verify=False)
soup = bs(r.text)
msg = soup.message.string.replace('Successful!,', '')
img = rs.get(f'https://www.cnsonline.com.tw/preview/GenerateImage?generalno=16014&version=zh_TW \
    &pageNum=5&checksum={msg}', headers=headers, verify=False)
print(type(img))

