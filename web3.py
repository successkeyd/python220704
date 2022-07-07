# web3.py
#웹서버에 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#파일에 저장
f = open("C:\\work\webtoon.txt", "wt", encoding="utf-8")
#수열을 생성해서 URL주소 만들기
try:
    for i in range(1,11):
        url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri&page=" + str(i)
        print(url)
        data = urllib.request.urlopen(url)
        soup = BeautifulSoup(data, "html.parser")

        cartoons = soup.find_all("td", class_="title")

        for item in cartoons:
            title = item.find("a").text
            print(title.strip())
            f.write(title + "\n")

    f.close()
    print("웹 크롤링 종료")
except:
    pass

