class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says meow!")
class Dog:
    """a dog"""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f"{self.name} says woof!")

millo = Dog("Millo")
millo.speak()

ella = Cat("Ella")
ella.speak()