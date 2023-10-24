class House():
    """"описание дома"""
    def __init__(self, street, number):
        """свойства дома"""
        self.street = street
        self.number = number
        self.age = 0

    def build(self):
        """строит дом"""
        print("Дом на улице " + self.street + " под номером " + self.number + " построен.")
    def age_of_house(self, year):
        """возраст дома"""
        self.age += year
class ProspectHouse(House):
    """дома на проспекте"""
    def __init__(self, prospect, number):
        super().__init__(self, number)
        self.prospect = prospect

PrHouse = ProspectHouse("Ленина", 5)
print(PrHouse.prospect)

