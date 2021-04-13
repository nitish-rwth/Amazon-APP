# This is a program to simulate user shopping experience on Amazon

from datetime import date
import hashlib
import pickle

# Class definitions for the main program


class Customer:
    def __init__(self, first_name, last_name, secure_password, email, age, address,
                 shopping_cart, account_type, order_confirmed):

        self.f_name = first_name
        self.l_name = last_name
        self.password = secure_password
        self.email = email
        self.age = age
        self.address = address
        self.order_list = shopping_cart
        self.type = account_type
        self.checkout = order_confirmed


class Product:
    def __init__(self, prod_name, quantity, order_date):
        self.prod_name = prod_name
        self.quantity = quantity
        self.order_date = order_date


class Checkout:
    def __init__(self, shopping_cart, checkout_date, user_email, user_address):
        self.product_list = shopping_cart
        self.date = checkout_date
        self.user_email = user_email
        self.address = user_address


# user_list = []

# Functions for data manipulation and storage


def pwd_encrypt(a):

    m = hashlib.sha256()
    m.update(a.encode())
    return m.hexdigest()


def database_read():
    user_list = []
    with open('database.pkl', 'rb') as file:
        while True:
            try:
                user_list = pickle.load(file)
                break
            except EOFError:
                break
        return user_list


def database_write(a):

    with open('database.pkl', 'wb') as file:
        pickle.dump(a, file, pickle.HIGHEST_PROTOCOL)


def read_top_deals():

    f = open("topdeals.txt", "r")
    for x in f:
        print(x)

    f.close()


# Function definitions for the user


def add_user():
    a = input("\n Enter your first name : ")
    b = input(" Enter your last name : ")
    c = input(" Enter your email : ")
    d = int(input(" Enter your age : "))
    e = input(" Enter your password : ")
    f = input(" Enter your address : ")
    g = input(" Please select an account type (prime/normal) : ")
    p = pwd_encrypt(e)

    if g == "prime" or g == "normal":
        new_user = Customer(a, b, p, c, d, f, [], g, [])
    else:
        print("\n Wrong account type entered!! Try again.")
        g = input(" Please select an account type (prime/normal) : ")
        new_user = Customer(a, b, p, c, d, f, [], g, [])

    old_user_list.append(new_user)
    print("\n Your user account has now been created!!")


def user_login(u):

    a = input("\n Enter your first name : ")
    b = input(" Enter your last name : ")
    c = input(" Enter your password : ")
    p = pwd_encrypt(c)

    for user in u:
        if a == user.f_name and b == user.l_name and p == user.password:
            print("\n You are now logged into your Amazon account!! \n")
            print("\t Welcome to Amazon,  " + user.f_name + " !")
            input("\n Press Enter to go to the user menu!")
            return user

    else:
        print("\n User account not found or wrong password!! Please create a new Amazon account or try again.")
        input(" Press Enter to return to the main menu!")
        return False


def user_logout():
    print("\n You are now logged out from your Amazon account!!")
    input("\n Press Enter to return to the main menu")


def false_user_login(counter):

    if counter == 3:  # Login fails after 3 unsuccessful attempts
        print("\n You have used your 3 allowed login attempts!")
        print(" Your account is now locked!! Please contact Amazon tech support for help.")
        return False


# Function definitions for the product


def add_order(b):
    o = "y"
    while o == "y":
        o = input("\n Do you want to add products to your cart? (y/n): ")

        if o == "y":

            c = input("\n Enter the product name : ")
            d = int(input("Enter the number of units to buy : "))
            e = date.today()
            print("Product added to cart on date : " + str(e))

            new_order = Product(c, d, e)
            b.order_list.append(new_order)
            print("\n The product has now been added to your cart!!")
            input("\n Press Enter to continue")

        elif o == "n":
            print("\n You will now return to the user menu!")

        else:
            print("\n Wrong choice entered! Try again")
            input("\n Press Enter to continue")


def display_order(b):
    if len(b.order_list) != 0:
        print("\n Your shopping cart has the following items: \n")
        i = 1
        for order in b.order_list:
            print(str(i) + ") Product name : " + order.prod_name + " , " + " Quantity : " + str(order.quantity))
            i += 1

    else:
        print("\n Your shopping cart is empty!!")
        input("\n Press Enter to go to user menu!")
        return False


def remove_order(b):

    display_order(b)

    choice = "y"
    while choice == "y":
        choice = input("\n Do you want to remove products from your cart? (y/n): ")
        if choice == "y":
            a = input("\n Enter the name of the product to be removed : ")

            for order in b.order_list:
                if a == order.prod_name:
                    b.order_list.remove(order)
                    print(order.prod_name + " has now been removed from your shopping cart!!")
                    input("\n Press Enter to go to main menu!")
                    break

        elif choice == "n":
            print("\n You will now be returned to the user menu!")
            break

        else:
            print("\n Wrong choice entered! Try again")
            input("\n Press Enter to continue")


# Function definitions for the Checkout

def confirm_order(b):

    final_order = Checkout(b.order_list, date.today(), b.email, b.address)
    b.checkout.append(final_order)
    b.order_list = []               # Shopping cart cleared
    print("\n Your shopping cart is now empty. All items in your shopping cart are now in checkout!!")
    print("\n You can now proceed to payment.")
    input("\n Press Enter to continue")
    return False


# Main Program starts here


print("\n Welcome to the Amazon Demo Program!!")
user1 = None
login_counter = 0

while True:

    old_user_list = database_read()         # Reading existing data from binary file and storing it in a local variable
    print("\n Please select an option from the main menu: ")
    print("\n 1. Create your user account")
    print(" 2. Log into your user account")
    print(" 0. Exit from this Demo program")

    choice1 = int(input("\n Enter your choice = "))

    if choice1 == 1:
        add_user()
        input("\n Press Enter to continue")

    elif choice1 == 2:

        user1 = (user_login(old_user_list))

        while user1 is not False and login_counter < 3:

            print("\n Please select an option from your user menu: \n")

            print("\n 1. Add a product to your shopping cart")
            print(" 2. Show top deals of the day")
            print(" 3. Display your shopping cart")
            print(" 4. Log out from your Amazon account")
            print(" 0. Exit from the demo program")

            choice2 = int(input("\n Enter your choice = "))

            if choice2 == 1:
                add_order(user1)

            elif choice2 == 2:
                print("\n Top deals available today are : \n")
                read_top_deals()
                choice4 = int(input("\n Enter your choice : "))

                if choice4 == 0:
                    continue
                else:
                    print("\n Wrong choice entered!! Please select a deal number or 0")
                    input(" Press Enter to continue...")
                    continue

            elif choice2 == 3:

                while display_order(user1) is not False:

                    input("\n Press Enter to go to the cart menu...")
                    print("\n Please select an option from your cart options- \n")

                    print("\n 1. Remove a product from your shopping cart")
                    print(" 2. Confirm order and checkout")
                    print(" 0. Go back to user menu")

                    choice3 = int(input("\n Please enter your choice : "))

                    if choice3 == 1:
                        remove_order(user1)

                    elif choice3 == 2:
                        while confirm_order(user1) is not False:
                            continue
                        else:
                            break

                    elif choice3 == 0:
                        input(" Press Enter to return to the user menu...")
                        break

                    else:
                        print("\n Wrong choice entered!! Please select a value between 0-2.")
                        input(" Press Enter to continue...")

            elif choice2 == 4:
                user_logout()
                user1 = None
                break

            elif choice2 == 0:
                print("\n The program will now exit!!")
                exit()

            else:
                print("\n Wrong choice entered!! Please choose an option from 1-5!")
                input("\n Press Enter to return to the main menu!")

        if user1 is False and login_counter < 3:
            login_counter += 1
            false_user_login(login_counter)

        else:
            print("\n Your Amazon account is now locked!! Please contact tech support for assistance.")

    elif choice1 == 0:
        print("\n The program will now exit!!")
        exit()

    else:
        print("\n Wrong choice entered!! Please enter a number between 0-2.")
        input(" Press Enter to go back to the main menu")

    database_write(old_user_list)
