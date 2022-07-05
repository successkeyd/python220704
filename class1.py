# class1.py
#1)클래스 형식을 정의

class Person:
    #초기화 메소드(생성자)
    def __init__(self):
        #인스턴스 멤버 변수
        self.name = "default name"
    #인스턴스 메소드
    def print(self):
        print("My name is {0}".format(self.name))

#2)인스턴스 생성
p1 = Person()
p2 = Person()
p2.name = "전우치"

#3)메소드 호출
p1.print()
p2.print()

#런타임(실행시간)에 변수를 추가 --> 동적 형식의 언어
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)
