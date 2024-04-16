class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def check_adult(self):
        if self.age >= 20:
            print(f"{self.name}は大人である")
        else:
            print(f"{self.name}は大人ではない")

humans = [
    Human("A", 25),
    Human("B", 18),
    Human("C", 30),
    Human("D", 16)
]

for person in humans:
    person.check_adult()
