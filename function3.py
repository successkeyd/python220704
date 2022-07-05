# function3.py
#교집합 함수
def intersect(prelist, postlist):
    #교집합 문자를 담을 지역변수 리스트
    result = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #특정 글자가 postlist에 있고 그러면서 글자가 아직 result에 없는 경우
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersect("HAM","SPAM"))
