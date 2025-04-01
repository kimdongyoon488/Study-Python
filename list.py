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