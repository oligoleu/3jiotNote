from bs4 import BeautifulSoup as bs

import requests as rs
bookid='16014'
headers = {'Content-Type':'application/x-www-form-urlencoded'}
def getToken(pn):
    content = f'generalno={bookid}&version=zh_TW&pageNum={pn}&pages=139'

    r = rs.post('https://www.cnsonline.com.tw/preview/GetData', data=content, headers=headers, verify=False)
    soup = bs(r.text)
    msg = soup.message.string.replace('Successful!,', '')

    return msg
def getPage(book,pn,token):
    img = rs.get(f'https://www.cnsonline.com.tw/preview/GenerateImage?generalno={bookid}&version=zh_TW&pageNum={pn}&checksum={token}', verify=False)

    if img.status_code == 200:
        # make relative path book/{bookid}/ first
        with open('./book/%s/book.%s.P.%04d.jpg'%(book,book,pn), 'wb') as f:
            for chunk in img:
                f.write(chunk)
if __name__ == "__main__" :
    for pn in range(1,139):
        tok=getToken(pn)
        getPage(bookid,pn,tok)
