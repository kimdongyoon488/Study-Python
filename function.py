def print_2_dan():
    dan = 2
    print(f"== {dan}단 ==")
    i = 1
    while i <= 9:
        print(f"{dan} * {i} = {dan * i}")
        i += 1

print_2_dan();


#매개변수
def print_dan(dan):
   i = 1
   while i <= 9:
       print("{} *  {}".format(dan, i, dan * i))
       i += 1

print_dan(2);