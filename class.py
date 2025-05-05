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