# db1.py
import sqlite3

#메모리에서 작업(약간의 약속된 문자열)
con = sqlite3.connect(":memory:")
#커서객체를 리턴
cur = con.cursor()
#데이터를 저장할 테이블 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")

#검색
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)
