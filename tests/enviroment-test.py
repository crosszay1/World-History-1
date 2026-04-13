class character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.happiness = 100 #100%
        

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."