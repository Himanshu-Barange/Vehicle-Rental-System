from datetime import datetime
from Booking import Booking


class Payment:
    def __init__(self, payment_id: int, booking: Booking, amount: float):
        self.paymentID = payment_id
        self.booking = booking
        self.paymentDate = datetime.now()
        self.amount = amount

    def refund(self):
        # Note: This simply marks the payment for a refund. Actual refunding would involve more logic.
        self.amount = -self.amount
