class Dog(object):
    def __init__(self, name, age):
        self.name = name  # Attributes
        self.age = age   # Attributes

    def speak(self):  # Methods
        print("Hi I am ", self.name, 'and I am ', self.age, 'years old!! ')

    def change_age(self, age):
        self.age = age


dog1 = Dog('Tim', '1')
dog2 = Dog('Fred', '2')

dog1.change_age(3)

dog1.speak()
dog2.speak()
