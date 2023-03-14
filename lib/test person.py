class Dog:
    def __init__(self, name, favorite_toy="Any"):
        self.name = name
        self.favorite_toy = favorite_toy
    def bark(self):
        print("woof!")
    def get_adopted(self, owner_name):
        self.owner = owner_name

fido = Dog("Fido")
fido.get_adopted("Sophie")

print(fido.favorite_toy)
