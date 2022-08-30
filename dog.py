class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age


d0 = Dog('Tim', 8)
print(d0.get_name())

d1 = Dog('Bill', 16)
print(d1.get_age())
d1.set_age(10)  # muda age
print(d1.get_age())
