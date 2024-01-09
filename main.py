# from FORMS import create_app
#
# app = create_app()
#
# if __name__ == "__main__":
#     app.run(debug=True)

from FORMS.models.businesses import Business


def login():
    print("You are in login function")

    email = input("Enter email:")
    password = input("Enter password")

    if Business.authenticate(email, password):
        print("Authentication successful!")
    else:
        print("Authentication failed. Please check your credentials.")

def validate_save_business():
    name = "John Doe"
    address = "123 Main St"
    email = 'john.doe@example.com'
    phone = "1234567890"
    sub_plan = "Basic"
    industry = "Technology"
    password = "securepassword"
    is_active = True
    is_deleted = False

    business1 = Business(name, address, email, phone, sub_plan, industry, password, is_active, is_deleted)

    business1.validate_and_insert_into_database()


if __name__ == "__main__":
    # validate_save_business()

    option = input("Enter one of the option to perform: "
                   "\n 1 for login"
                   "\n 2 for new business")

    match option:
        case "1":
            login()
        case "2":
            validate_save_business()
        case _:
            print("Invalid option")
