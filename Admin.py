from Feedback import Feedback
from Maintenance import Maintenance
from database import customers, vehicles, bookings, payments


class Admin:
    @staticmethod
    def view_all_customers():
        return customers

    @staticmethod
    def view_all_vehicles():
        return vehicles

    @staticmethod
    def view_all_bookings():
        return bookings

    @staticmethod
    def view_all_payments():
        return payments

    @staticmethod
    def view_all_feedback():
        return Feedback.feedback_records

    @staticmethod
    def view_all_maintenance_records():
        return Maintenance.maintenance_records
