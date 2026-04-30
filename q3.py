class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"a Cat names {self.name}"
    def speak(self):
        print(f"{self.name} says meow!")
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"a Dog names {self.name}"
    def speak(self):
        print(f"{self.name} says woof!")

millo = Dog("Millo")
millo.speak()

ella = Cat("Ella")
ella.speak()