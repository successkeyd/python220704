# DemoFile.py
#파일 쓰기
f = open("C:\\work\\demo.txt", "wt")
f.write("첫번째\n두번째\n세번째라인\n")
f.close()

print("C:/work/test.txt")
#raw string notation(날것 그대로 가공안함) C#(@)
print(r"C:\work\newfile.txt")

#파일 읽기
f = open("C:\\work\\demo.txt", "rt")
result = f.read()
print(result)
#파일 포인터의 위치
print(f.tell())
#다시 처음으로 이동(리셋)
f.seek(0)
print(f.readline(), end="\n")
print(f.readline(), end="\n")

    
f.close()



with open("C:\\work\\demo.txt", "a+") as f:
    f.write("새로운 데이터\n")
