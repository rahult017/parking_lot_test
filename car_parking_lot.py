import random
import json


class ParkingLot:
    def __init__(self, square_footage, spot_size=(8, 12)):
        # Calculate the capacity based on square footage and spot size
        self.capacity = int(square_footage / (spot_size[0] * spot_size[1]))
        # Initialize an array to represent parking spots, initially all empty (None)
        self.spots = [None] * self.capacity

    def park_vehicle(self, vehicle, spot_number):
        # Check if the spot is empty, then park the vehicle
        if self.spots[spot_number] is None:
            self.spots[spot_number] = vehicle
            return True
        # If the spot is occupied, return False to indicate unsuccessful parking
        return False
    
    def is_full(self):
        # Check if all spots are occupied
        return all(spot is not None for spot in self.spots)

    def map_to_json(self):
        # Create a dictionary mapping spot numbers to vehicle license plates
        return {str(i): str(v) for i, v in enumerate(self.spots) if v is not None}

class Car:
    def __init__(self, license_plate):
        # Initialize a car with a given license plate
        self.license_plate = license_plate

    def __str__(self):
        # Magic method to convert the car instance to a string (returns the license plate)
        return self.license_plate

    def park(self, parking_lot, spot_number):
        # Attempt to park the car in the specified spot in the parking lot
        if parking_lot.park_vehicle(self, spot_number):
            print(f"Car with license plate {self.license_plate} parked successfully in spot {spot_number}")
            return True
        else:
            print(f"Failed to park car with license plate {self.license_plate} in spot {spot_number}")
            return False

def main():
    # Create a parking lot with a specific square footage and spot size
    parking_lot = ParkingLot(2000, spot_size=(10, 15))
    # Create a list of cars with random license plates
    cars = [Car(f"ABC{random.randint(1000, 9999)}") for _ in range(20)]  # Example usage

    while cars:
        # Take a car from the list
        car = cars.pop()
        # Generate a random spot number to attempt parking
        spot_number = random.randrange(parking_lot.capacity)
        
        # Try to park the car until successful
        while not car.park(parking_lot, spot_number):
            # If unsuccessful, generate a new spot number until the car is parked
            spot_number = random.randrange(parking_lot.capacity)
            
            # Check if the parking lot is full and exit the loop if so
            if parking_lot.is_full():
                print("Parking lot is full.")
                break

    # Optional bonus task: Save the mapping of vehicles to spots in a JSON file
    parking_json = parking_lot.map_to_json()
    with open("parking_data.json", "w") as f:
        json.dump(parking_json, f)

if __name__ == "__main__":
    main()
