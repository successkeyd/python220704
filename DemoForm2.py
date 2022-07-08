# DemoForm2.py
# DemoForm2.py(로직) + DemoForm2.ui(화면단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
#웹서버에 요청
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#디자인 파일을 로딩(DemoForm2)
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼클래스 정의(QMainWindow를 상속, 변경)
class DemoForm(QMainWindow, form_class):
    #생성자 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    
    def firstClick(self):
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
            self.label.setText("네이버 웹툰 크롤링 종료")
        except:
            pass        
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭")

#진입점 체크
if __name__ == "__main__":
    #실행프로세스 생성
    app = QApplication(sys.argv)
    #화면생성
    demoWindow = DemoForm()
    demoWindow.show()
    #이벤트 대기
    app.exec_()

    