from datetime import datetime
from Customer import Customer


class Feedback:
    feedback_records = []

    def __init__(self, customer: Customer, content: str, rating: int):
        self.customer = customer
        self.content = content
        self.date = datetime.now()
        if 1 <= rating <= 5:
            self.rating = rating
        else:
            self.rating = 3  # Default rating if out of range
        Feedback.feedback_records.append(self)

    @staticmethod
    def submit_feedback(customer, content, rating):
        feedback = Feedback(customer, content, rating)
        return "Feedback submitted successfully!"
