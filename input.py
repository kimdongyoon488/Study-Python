#문제 - 사용자에게 문장 1개를 입력받아서, 출력하시오

user_input = input("문장 하나를 입력해주세요 : ")

print(f"입력 된 내용 : {user_input}")



#문제 - 사용자에게 숫자 2개를 입력받아서, 더한 결과를 출력하시오

print("숫자 2개르 입력해주세요. : ", end = '')
user_input = input().strip().split('')

user_input[0] = int(user_input[0])
user_input[1] = int(user_input[1])

print(user_input[0] + user_input[1])