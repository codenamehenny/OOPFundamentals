#Task 1: Vehicle Registration System
#- Problem Statement: Create a Python class Vehicle with attributes registration_number, type, and owner. 
# Implement a method update_owner to change the vehicle's owner. 
# Then, create a few instances of Vehicle and demonstrate changing the owner.

class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.reg_num = reg_num
        self.vehicle_type = vehicle_type
        self.owner = owner
    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"\n{new_owner} updated to the registration system")
    def display_info(self):
        print(f"\nRegistration: {self.reg_num} | Vehicle Type: {self.vehicle_type} | Owner: {self.owner}")

vehicles = {}

def register_vehicle(reg_num, vehicle_type, owner): 
    if reg_num in vehicles:
        print(f"\nRegistration number {reg_num} already in the system")
    else:
        vehicles[reg_num] = Vehicle(reg_num, vehicle_type, owner)
        print(f"\nRegistration number {reg_num} added to the system")

def update_vehicle_owner(reg_num, new_owner):
    if reg_num in vehicles:
        vehicles[reg_num].update_owner(new_owner)
        print(f"\nOwner for registration number {reg_num} updated to {new_owner}")
    else:
        print(f"\nRegistration number {reg_num} not found") 

def display_vehicles():
    if vehicles:
        for vehicle in vehicles.values():
            vehicle.display_info()
    else:
        print("Registration system empty")

while True:
    option = input("Welcome to the vehicle registration system!\nWould you like to register, update, display or exit? ").lower()
    try:
        if option == "register":
            reg_num = input("Enter the registration number: ")
            vehicle_type = input("Enter vehicle type (car, bike, boat, etc.): ")
            owner = input("Enter vehicle owner's name: ")
            register_vehicle(reg_num, vehicle_type, owner)
        elif option == "update":
            reg_num = input("Enter the registration number: ")
            new_owner = input("Enter the new owner name: ")
            update_vehicle_owner(reg_num, new_owner)
        elif option == "display":
            display_vehicles()
        elif option == "exit":
            print("Thanks for using the vehicle registration. Goodbye")
            break
    except Exception as e:
        print(f"\nError message '{e}'. Please try again")
