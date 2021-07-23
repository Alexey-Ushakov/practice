class Person:
    name = "default name"
    mana = 150
    health = 250
    def __init__(self, *args, **kwargs):
        if "name" in kwargs:
            self.name = kwargs.get("name")
        if "mana" in kwargs:
            self.name = kwargs.get("mana")
        if "health" in kwargs:
            self.name = kwargs.get("health")

    # def show_info(self):
    #     print(self.name, Person.mana, Person.health)

a = Person({"mana"=5,"name"="Pirs"})

# a.show_info()
print(a.name, a.mana, a.health)


