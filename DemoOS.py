# DemoOS.py
from os.path import *

#print(dir())
print(abspath("python.exe"))
print(basename("c:\\work\\ptyhon.exe"))
print(exists("c:\\python39\\python.exe"))
print(getsize("c:\\python39\\python.exe"))

from os import *
#실행 파일 실행
##system("notepad.exe")
print("운영체제:", name)

#파일 목록
import glob
result = glob.glob("c:\\work\\*.py")

for item in result:
    print(item)



    