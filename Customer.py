from Booking import Booking
from datetime import datetime
from database import customers, bookings, payments


class Customer:

    def __init__(self, customer_id: int, name: str, email: str, password: str):
        self.customerID = customer_id
        self.name = name
        self.email = email
        self._password = password  # In a real-world system, never store passwords in plain text!
        self.registeredDate = datetime.now()
        self.loyaltyPoints = 0

    @classmethod
    def register(cls, name: str, email: str, password: str):
        """Register a new customer."""

        # denying duplicate emails
        for customer in customers:
            if customer.email == email:
                print("Email already registered. \nUse a different email or login with the registered email.")
                return None

                # password should be at least this lengthy
                # password should contain both alphabets and numerics
        min_password_len = 8
        if len(password) < min_password_len:
            print(f'Password must be of at least {min_password_len}characters.')
            return None
        if not any(char.isalpha() for char in password) or not any(char.isdigit() for char in password):
            print('Password must contain both letters and numbers.')
            return None

        customer_id = len(customers) + 1
        new_customer = cls(customer_id, name, email, password)
        customers.append(new_customer)
        return new_customer

    @staticmethod
    def login(email, password):
        """Login to you account."""
        for customer in customers:
            if customer.email == email and customer.password == password:
                return True
        return False

    def get_password(self):
        return self._password

    def book_vehicle(self, vehicle, start_date, end_date):
        if vehicle.checkAvailability():
            booking_id = len(bookings) + 1
            new_booking = Booking(booking_id, self, vehicle, start_date, end_date)
            bookings.append(new_booking)
            vehicle.updateAvailability(False)
            return new_booking
        else:
            print("Vehicle is not available!")
            return None

    def view_booking(self):
        """View all booking made by a customer."""
        my_bookings = [booking for booking in bookings if booking.customer == self]
        return my_bookings

    def view_payments(self):
        """View all payments made a customer."""
        my_payments = [payment for payment in payments if payment.booking.customer == self]
        return my_payments

    def earn_loyalty_points(self, amount):
        """Earn 1 point for every $10 spent."""
        self.loyaltyPoints += amount // 10

    def redeem_loyalty_points(self):
        """Every loyalty point gives a $0.5 discount."""
        discount = self.loyaltyPoints * 0.5
        self.loyaltyPoints = 0
        return discount
