class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"저는 {self.name} 이고 나이는 {self.age}살 입니다")

p1 = Person("김동윤", 25)

print(p1.name)
print(p1.age)
print(p1.introduce())


#문제:
#동물(Animal) 클래스를 만들고, 이 클래스는 모든 동물이 공통적으로 가지고 있는 `eat()` 메서드를 가집니다.
#`eat()` 메서드는 "동물이 음식을 맛있게 먹습니다."라는 메시지를 출력합니다.

#그 다음에, `Dog`와 `Cat` 클래스를 `Animal` 클래스의 자식 클래스로 만듭니다.
#`Dog` 클래스와 `Cat` 클래스는 각각 `eat()` 메서드를 오버라이딩하여,
#각각 "강아지가 밥을 먹습니다."와 "고양이가 밥을 먹습니다."라는 메시지를 출력하도록 합니다.

#이 문제를 해결하는 파이썬 코드를 작성하십시오.


class 동물():
    def eat(self):
        print("동물이 음식을 맛있게 먹습니다.")

# 강아지 is a 동물 : 강아지는 동물이야
class 강아지(동물):
    def eat(self):
        print("강아지가 밥을 먹습니다.")

class 고양이(동물):
    def eat(self):
        print("고양이가 밥을 먹습니다.")

dog = 강아지()
dog.eat()

cat = 고양이()
cat.eat()




