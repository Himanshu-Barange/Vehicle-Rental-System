# Assuming all the classes and implementations from previous parts are loaded...
from Customer import Customer
from Vehicle import Vehicle
from Booking import Booking
from Feedback import Feedback
from Maintenance import Maintenance
from Admin import Admin
from database import customers, vehicles, bookings, payments
from datetime import datetime


def main_menu():
    print("Welcome to the Vehicle Rental System!")
    print("1. Register as a new customer")
    print("2. Customer login")
    print("3. Admin tasks")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice


def customer_menu():
    print("Customer Menu:")
    print("1. View available vehicles")
    print("2. Book a vehicle")
    print("3. View my bookings")
    print("4. View my payments")
    print("5. Submit feedback")
    print("6. Redeem loyalty points")
    print("7. Logout")
    choice = input("Enter your choice: ")
    return choice


def admin_menu():
    print("Admin Menu:")
    print("1. View all customers")
    print("2. View all vehicles")
    print("3. View all bookings")
    print("4. View all payments")
    print("5. View all feedback")
    print("6. View all maintenance records")
    print("7. Logout")
    choice = input("Enter your choice: ")
    return choice


def customer_login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    for customer in customers:
        if customer.email == email and customer.get_password == password:
            return customer
    print("Invalid credentials!")
    return None


def main():
    while True:
        choice = main_menu()

        if choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            customer = Customer.register(name, email, password)
            if customer:
                print("Registration successful!")

        elif choice == '2':
            customer = customer_login()
            if customer:
                while True:
                    c_choice = customer_menu()

                    if c_choice == '1':
                        available_vehicles = Vehicle.search_available_vehicles()
                        for vehicle in available_vehicles:
                            print(vehicle)

                    elif c_choice == '2':
                        vehicle_id = int(input("Enter vehicle ID to book: "))
                        start_date = input("Enter start date (YYYY-MM-DD): ")
                        end_date = input("Enter end date (YYYY-MM-DD): ")
                        customer.bookVehicle([v for v in vehicles if v.vehicleID == vehicle_id][0],
                                             datetime.strptime(start_date, "%Y-%m-%d"),
                                             datetime.strptime(end_date, "%Y-%m-%d"))
                        print("Vehicle booked successfully!")

                    elif c_choice == '3':
                        for booking in bookings:
                            if booking.customer == customer:
                                print(booking)

                    elif c_choice == '4':
                        payments_by_customer = customer.viewPayments()
                        for payment in payments_by_customer:
                            print(payment)

                    elif c_choice == '5':
                        content = input("Enter your feedback: ")
                        rating = int(input("Rate our service (1-5): "))
                        Feedback.submit_feedback(customer, content, rating)
                        print("Feedback submitted!")

                    elif c_choice == '6':
                        redeem_value = customer.redeemLoyaltyPoints()
                        print(
                            f"Successful redemption of loyalty points for a ${redeem_value} discount on next booking!")

                    elif c_choice == '7':
                        break

                    else:
                        print("Invalid choice!")

        elif choice == '3':
            # For simplicity, we assume the admin does not require a login in this example
            while True:
                a_choice = admin_menu()

                if a_choice == '1':
                    for c in Admin.view_all_customers():
                        print(c)

                elif a_choice == '2':
                    for v in Admin.view_all_vehicles():
                        print(v)

                elif a_choice == '3':
                    for b in Admin.view_all_bookings():
                        print(b)

                elif a_choice == '4':
                    for p in Admin.view_all_payments():
                        print(p)

                elif a_choice == '5':
                    for f in Admin.view_all_feedback():
                        print(f)

                elif a_choice == '6':
                    for m in Admin.view_all_maintenance_records():
                        print(m)

                elif a_choice == '7':
                    break

                else:
                    print("Invalid choice!")

        elif choice == '4':
            print("Thank you for using the Vehicle Rental System!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
