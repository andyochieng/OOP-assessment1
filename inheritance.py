class Animal:
    def eat(self):
        print('Eating')

    def sleep(self):
        print('Sleeping')

class Dog(Animal):
    def bark(self):
        print('Barking')

my_dog = Dog()
my_dog.eat()
my_dog.sleep()

my_dog.bark()