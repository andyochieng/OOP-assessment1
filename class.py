class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"car make: {self.make}")
        print(f"car model: {self.model}")
        print(f"car year: {self.year}")

my_car = Car("NISAAN", "Teana", "2011")
my_car.display_info()
