# Assignment 1: Design class smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery_life = battery_life  # in hours

    def make_call(self, number):
        print(f"Dialing {number} using {self.model}...")

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.model}...")

    def __str__(self):
        return f"{self.brand} {self.model} - {self.storage}GB, {self.battery_life}h battery life"

# Adding inheritance for polymorphism
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, gpu):
        super().__init__(brand, model, storage, battery_life)
        self.gpu = gpu

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.model} with {self.gpu} GPU.")

    def __str__(self):
        return f"{self.brand} {self.model} (Gaming Edition) - {self.storage}GB, {self.battery_life}h battery life, {self.gpu} GPU"

# Test the classes
if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 14", 128, 20)
    print(phone)
    phone.make_call("123-456-7890")
    phone.install_app("Instagram")

    gaming_phone = GamingSmartphone("Asus", "ROG Phone 6", 256, 30, "Adreno 730")
    print(gaming_phone)
    gaming_phone.play_game("Genshin Impact")

# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")

# Test the polymorphism
vehicles = [Car(), Plane(), Boat()]
for vehicle in vehicles:
    vehicle.move()
