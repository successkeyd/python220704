# -*- 생성자와 소멸자 -*-
class MyClass:
    #가장 먼저 실행되는 초기화 메서드
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    #가장 마지막에 청소하는 작업 메서드
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성
d = MyClass(5)
# del d

print("전체 코드 실행 종료")