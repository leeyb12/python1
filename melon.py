import requests as bs
from bs4 import BeautifulSoup as bs
url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36 Edg/133.0.0.0'}
web = requests.get(url, headers = headers)
def mel():
    soup = bs(web.content, 'html.parser')
    title = soup.select('.rank01')
    name = soup.select('.checkEllipsis a')
    str = ''
    for i, (t,n) in enumerate(zip(title, name),1):
        str += f'{i}위:{t.text.strip()}/{n.text}\n'
    print(str,end=' ')

if __name__ == '__main__':
    mel()