from datetime import datetime
from Customer import Customer
from Vehicle import Vehicle
from Payment import Payment
from database import customers, vehicles, bookings, payments


class Booking:
    def __init__(self, booking_id: int, customer: Customer, vehicle: Vehicle, start_date: datetime, end_date: datetime):
        self.booking_id = booking_id
        self.customer = customer
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date
        # Assuming the totalPrice will be calculated based on days and vehicle's rental price
        self.total_price = self.calculate_price()

    def calculate_price(self):
        """Provides rental price of a vehicle based on hire period."""
        days = (self.end_date - self.start_date).days
        return days * self.vehicle.get_rental_price()

    def cancel_booking(self):
        """Cancel a booked vehicle"""
        self.vehicle.update_availability(True)
        bookings.remove(self)

    def make_payment(self, amount):
        """Make payment for a booking."""
        payment_id = len(payments) + 1
        new_payment = Payment(payment_id, self, amount)
        payments.append(new_payment)
        return new_payment

    def modify_booking(self, start_date: datetime, end_date: datetime):
        """Make changes to a booking."""
        if self.vehicle.check_availability():
            self.start_date = start_date
            self.end_date = end_date
            self.total_price = self.calculate_price()
        else:
            raise Exception("Cannot modify booking. Vehicle is not available for the chosen dates.")

            # can be further enhanced to take discount between 0 and 1

    def apply_discount(self, percentage: float):
        """Apply discount on a booking price."""
        if not (0 < percentage < 100):
            raise ValueError("Invalid discount percentage.")
        discount_amount = (percentage / 100) * self.total_price
        self.total_price -= discount_amount
        self.customer.earn_loyalty_points(discount_amount)
