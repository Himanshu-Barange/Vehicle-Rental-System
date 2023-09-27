from datetime import datetime
from Vehicle import Vehicle


class Maintenance:
    maintenance_records = []

    def __init__(self, vehicle: Vehicle, start_date: datetime, end_date: datetime, description: str):
        self.vehicle = vehicle
        self.startDate = start_date
        self.endDate = end_date
        self.description = description
        Maintenance.maintenance_records.append(self)

    @staticmethod
    def schedule_maintenance(vehicle, start_date, end_date, description):
        record = Maintenance(vehicle, start_date, end_date, description)
        vehicle.update_availability(False)  # Setting the vehicle as unavailable during maintenance
        return record

    @staticmethod
    def complete_maintenance(record):
        record.vehicle.update_availability(True)
        return "Maintenance completed for Vehicle ID {}".format(record.vehicle.vehicleID)
