from datetime import datetime

from FORMS.models.sql_database_manager import sql_database_manager
import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv


# database_url = os.getenv("DATABASE_URL")
# api_key = os.getenv("API_KEY")


class Business:

    def __init__(self, name, address, email, phone, sub_plan, industry, password, is_active, is_deleted):

        self.name = name
        self.address = address
        self.date_of_creation = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Include date and time
        self.email = email
        self.phone = phone
        self.sub_plan = sub_plan
        self.industry = industry
        self.password = password
        self.is_active = is_active
        self.is_deleted = is_deleted
        self.db_manager = sql_database_manager()

    @staticmethod
    def validate_name(name):
        if not name:
            raise ValueError("Name cannot be empty.")
        # Add additional validation if needed
        return name

    @staticmethod
    def validate_email(email):
        # Basic email validation; you may use a regex or a library for more robust validation
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        # Add additional validation if needed
        return email

    @staticmethod
    def validate_phone(phone):
        # Basic phone number validation; you may use a regex for more robust validation
        if not phone.isdigit() or len(phone) < 10:
            raise ValueError("Invalid phone number.")
        # Add additional validation if needed
        return phone

    @staticmethod
    def validate_password(password):
        # Implement password strength requirements; this is just a basic example
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        # Add additional validation if needed
        return password

    def validate_and_insert_into_database(self):
        # db_manager = sql_database_manager()
        try:
            # Validate fields
            self.validate_name(self.name)
            self.validate_email(self.email)
            self.validate_phone(self.phone)
            self.validate_password(self.password)

            # Insert into the database
            self.insert_into_database()
            print("Business record inserted successfully.")
        except ValueError as e:
            print(f"Validation error: {e}")
            # Handle the validation error (e.g., provide feedback to the user)

    def insert_into_database(self):
        try:
            # Assuming you have a method like execute_query in your database manager
            query = """
                INSERT INTO businesses
                (name, address, date_of_creation, email, phone, sub_plan, industry, password, is_active, is_deleted)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            params = (
                self.name, self.address, self.date_of_creation, self.email,
                self.phone, self.sub_plan, self.industry, self.password, self.is_active, self.is_deleted
            )

            # Connect to the database
            self.db_manager.connect()

            # Execute the insert query
            self.db_manager.execute_query(query, params)

            # Commit the changes
            self.db_manager.connection.commit()

        except Exception as e:
            print(f"Error inserting into the database: {e}")
        finally:
            # Disconnect from the database
            self.db_manager.disconnect()

    def update_contact_information(self, new_contact_person, new_email, new_phone):
        """
        Update contact information for the business.
        """
        self.contact_person = new_contact_person
        self.email = new_email
        self.phone = new_phone

    def change_address(self, new_address):
        """
        Change the business address.
        """
        self.address = new_address

    def change_subscription_plan(self, new_sub_plan):
        """
        Change the subscription plan of the business.
        """
        self.sub_plan = new_sub_plan

    @staticmethod
    def authenticate(email, password):

        connection = sql_database_manager()

        connection.connect()

        # Assuming you have a 'business' table with columns 'business_email' and 'password'
        query = 'SELECT password FROM businesses WHERE email = %s;'
        cursor = connection.execute_query(query, (email,))

        result = cursor.fetchone()

        # Close the database connection
        connection.disconnect()

        if result is not None and result[0] == password:
            return True
        else:
            return False

#     def update_database_contact_information(self):
#
#     # Use the database manager to update the contact information in the database
#     # Example: db_manager.update("businesses", {"contact_person": self.contact_person, "email": self.email, "phone": self.phone}, f"business_id = {self.business_id}")
#
#     def update_database_address(self):
#
#     # Use the database manager to change the address in the database
#     # Example: db_manager.update("businesses", {"address": self.address}, f"business_id = {self.business_id}")
#
#     def update_database_subscription_plan(self):
# # Use the database manager to change the subscription plan in the database
# # Example: db_manager.update("businesses", {"sub_plan": self.sub_plan}, f"business_id = {self.business_id}")
#
