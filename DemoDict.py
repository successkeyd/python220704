# DemoDict.py
from os import device_encoding


device = {"아이폰":5, "아이패드":10, "윈도우":20}
print(len(device))
device["아이폰"] = 6
print(device["아이폰"])
device["맥북"] = 15
print(device)
del device["아이패드"]
print(device)

for item in device.items():
    print(item)

print("----------------")

for k,v in device.items():
    print(k,v)

#참조를 복사해서 전달
device2 = device
device2["애플워치"] = 20
print(device)
print(device2)
print(id(device))
print(id(device2))

isRight = True
print(type(isRight))
print(1 < 2)
print(1 != 2)
print(1 == 2)
