a = [1, 2, 3] # 리스트 초기화
print(a)

a.append(4) # 값 추가 : append(value)
print(a)

a.insert(0, 5) # 0번째 index에 5추가
print(a)

a.remove(5) #리스트에 특정 요소값 삭제 : remove(values)
print(a)

del a[1] # index가 1번째인 요소값을 삭제
print(a)

a[0] = 10 # 0번째 index를 10으로 수정
print(a)

print(len(a)) # 리스트의 길이 알려주는 함수 : len(var)

print(a.index(10)) # 해당 요소값의 위치 알려주는 함수 : index(var)


#문제 : 비어있는 리스트를 만들고, 순서대로 2, 1, 5, 6, 7를 하나씩 담아주세요

a = []
a.append(2)
a.append(1)
a.append(5)
a.append(6)
a.append(7)

print(a)

#문제 : 리스트에 순서대로 월, 화, 수 ,목 ,금을 한번에 담고
# 토,일 을 순서대로 추가해주세요.

a = ['월','화','수','목','금']
a.append('토')
a.append('일')

print(a)


#문제 : 리스트에 순서대로 월, 화, 수 ,목 ,금을 한번에 담고
# 토,일 을 담은 리스트를 만든 후 2개의 리스트를 합쳐서 새로운 리스트를 만들어주세요.

a = ['월','화','수','목','금']
b = ['토', '일']

#리스트 연산
print(a + b)