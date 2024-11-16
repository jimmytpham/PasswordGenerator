# Jimmy Pham
# T00629354
# COMP 2211

def main():
    # user input for first name, last name, and ID number
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    id_number = input("Enter your student number: ")
    print("Username: ", get_login_name(first_name, last_name, id_number))

    # User input for password
    password = input("Create a password: ")
    check_password(password)

    # Prints Login information
    print('\nLogin Information:')
    print('Username:', get_login_name(first_name, last_name, id_number))
    print('Password:', password)


def get_login_name(first_name, last_name, id_number):
    # Slice first name, last name, and ID number for username
    login_name = first_name[0:3] + last_name[0:3] + id_number[-3:]
    return login_name


def check_password(password):
    # If loop for length under 7
    if len(password) >= 7:
        check_pass = password.strip()

        # set all flags to false
        upper = False
        lower = False
        number = False
        for i in check_pass:
            # sets flags to true if at least 1 character meets standards
            if i.isupper():
                upper = True
            if i.islower():
                lower = True
            if i.isnumeric():
                number = True
            if upper and lower and number:
                print("Password accepted")
                return

        # User to re-enter password if any of the criteria is not met
        print("Password must have at least 1 uppercase, 1 lowercase, and 1 number")
        password = input("Create a password: ")
        check_password(password)
    else:

        # User to re-enter password if it is too short
        print("Password is too short, must be greater than 7 characters")
        password = input("Create a password: ")
        check_password(password)


main()
