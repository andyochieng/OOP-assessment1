class House:
    def __init__(self, address):
        self.address = address
        self.rooms=[self.Room("Living Room"), self.Room("Wash Room")]

    class Room:
        def __init__(self, name):
            self.name = name

house= House('ABC 123 Street')
for room in house.rooms:
    print(f"{room.name} in {house}")