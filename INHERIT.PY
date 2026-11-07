class animal:
    def eat(self):
        print("i need KFC!")
    def sleep(self):
        print("give me some sleep!")
class dog(animal):
    def bark(self):
        print("woof woof go away or give me KFC or SLEEP!")
dog1=dog()
dog1.eat()
dog1.sleep()
dog1.bark()
