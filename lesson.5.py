class Animal:
    def move(self):
        print('двигается')


class Swimming(Animal):
    def move(self):
        print('плавает')


class Flying(Animal):
    def move(self):
        print('летает')


class Duck(Animal):
    def move(self):
        print('летает и плавает')

duck = Duck()
duck.move()

print("=======")
print(Swimming.__mro__)
Animal = Swimming()
Animal.move()