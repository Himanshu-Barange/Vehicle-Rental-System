from Maintenance import Maintenance
from database import customers, vehicles, bookings, payments


class Vehicle:
    def __init__(self, vehicle_id: int, type_: str, brand: str, model: str, rental_price: float):
        self.vehicleID = vehicle_id
        self.type = type_
        self.brand = brand
        self.model = model
        self.availability_status = True  # Assuming a vehicle is available when added to the system
        self.rental_price = rental_price

    def check_availability(self):
        """Check Vehicle Availability."""
        return self.availability_status

    def update_availability(self, status: bool):
        """Update Vehicle Availability."""
        self.availability_status = status

    def get_rental_price(self):
        """Obtain rental price for a vehicle."""
        return self.rental_price

    @classmethod
    def add_vehicle(cls, type_: str, brand: str, model: str, rental_price: float):
        """Add a new vehicle to the fleet."""
        vehicle_id = len(vehicles) + 1
        new_vehicle = cls(vehicle_id, type_, brand, model, rental_price)
        vehicles.append(new_vehicle)
        return new_vehicle

    @classmethod
    def search_available_vehicles(cls, type_: str = None, brand: str = None, model: str = None):
        """Obtain available vehicles list using optional filters."""
        available_vehicles = [v for v in vehicles if v.check_availability()]

        if type_:
            available_vehicles = [v for v in available_vehicles if v.type == type_]
        if brand:
            available_vehicles = [v for v in available_vehicles if v.brand == brand]
        if model:
            available_vehicles = [v for v in available_vehicles if v.model == model]

        return available_vehicles

    def get_maintenance_history(self):
        """Obtain maintenance history for a vehicle."""
        return [record for record in Maintenance.maintenance_records if record.vehicle == self]
