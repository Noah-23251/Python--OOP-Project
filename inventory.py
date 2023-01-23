# Import tabulate function
from tabulate import tabulate
# ========The beginning of the class==========


# Create class Shoe, with parameters for country, code, product, cost and quantity
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Function to return shoe cost
    def get_cost(self):
        return self.cost

    # Function to return shoe quantity
    def get_quantity(self):
        return self.quantity

    # Function to return shoe data as string
    def __str__(self):
        return f"""
Code:           {self.code}
Product:        {self.product}
Country:        {self.country}
Cost:           {self.cost}
Quantity:       {self.quantity}
"""


# =============Shoe list===========
shoe_list = []
# ==========Functions outside the class==============


# Function to read shoe data from the inventory text file, and append info to shoe_list. holding_list.pop(0) is used to
# header row, before the shoe list is populated
def read_shoes_data():
    holding_list = []
    with open("inventory.txt", "r") as inv_text:
        for line in inv_text:
            holding_list.append(line.strip("\n"))
    holding_list.pop(0)
    for item in holding_list:
        product_list = item.split(",")
        shoe_list.append(Shoe(product_list[0], product_list[1], product_list[2], product_list[3], product_list[4]))


# Function to add new shoes to the list
def capture_shoes():
    code_new = input("Please enter the product code of the shoes to be added ")
    country_new = input("Please enter the country of the shoes to be added ")
    prod_new = input("Please enter the product name of the shoes to be added ")
    cost_new = input("Please enter the cost of the shoes to be added ")
    quantity_new = input("Please enter the quantity of the shoes to be added ")
    new_shoe = Shoe(country_new, code_new, prod_new, cost_new, quantity_new)
    shoe_list.append(new_shoe)
    print(f"New shoe added: {prod_new}")


# Function to view all shoes in the list - it was interesting learning to use tabulate!
def view_all():
    print_list = []
    for i in range(len(shoe_list)):
        print_list.append((shoe_list[i].country, shoe_list[i].code, shoe_list[i].product, shoe_list[i].cost,
                          shoe_list[i].quantity))
    print(tabulate(print_list, headers=["Country", "Code", "Product", "Cost", "Quantity"]))
    pass


# Function to return the lowest stock shoe and give the option to add additional stock - the shoe data is updated
# accordingly if additional stock is added
def re_stock():
    quantity_dict = {}
    min_shoe_index = 0
    for i in range(len(shoe_list)):
        quantity_dict[shoe_list[i].quantity] = shoe_list[i].code
        quantity_list = quantity_dict.keys()
        quantity_list_int = [int(a) for a in quantity_list]
        min_stock = min(quantity_list_int)
    print(f"The shoe with lowest stock is {quantity_dict[str(min_stock)]}, with only {min_stock} remaining")
    for j in range(len(shoe_list)):
        if shoe_list[j].quantity == str(min_stock):
            min_shoe_index = j
        else:
            pass
    while True:
        add_stock = input("Would you like to order additional stock this model? ").lower()
        if add_stock == "yes":
            try:
                stock_increase = int(input("Please enter the quantity of shoes to be added "))
            except ValueError:
                print("Error: Please enter a numerical value")
            shoe_list[min_shoe_index].quantity = min_stock + stock_increase
            break
        elif add_stock == "no":
            break
        else:
            print("Input not recognised. Please enter yes or no to proceed")
    pass


# Function to search for shoe by the shoe code
def search_shoe():
    code_list = []
    for i in range(len(shoe_list)):
        code_list.append(shoe_list[i].code)
    shoe_request = input("Please enter the code of the shoe you are searching for ").upper()
    while True:
        if shoe_request in code_list:
            break
        else:
            shoe_request = input("Code not recognised, please re-enter the code of the shoe you are searching for ").upper()
    request_index = 0
    for i in range(len(shoe_list)):
        if shoe_list[i].code == shoe_request:
            request_index = i
        else:
            pass
    print(shoe_list[request_index])

    pass


# Function to display the total value for each shoe model (cost * quantity) - tabulate again, it makes things so much
# prettier!
def value_per_item():
    value_list = []
    for i in range(len(shoe_list)):
        value_list.append(tuple((shoe_list[i].code, ((int(shoe_list[i].cost)) * (int(shoe_list[i].quantity))))))
    print(tabulate(value_list, headers=["Shoe Code", "Total Value"]))
    pass


# Function to return the shoe with the highest quantity
def highest_qty():
    quantity_dict = {}
    for i in range(len(shoe_list)):
        quantity_dict[shoe_list[i].quantity] = shoe_list[i].code
        quantity_list = quantity_dict.keys()
        quantity_list_int = [int(a) for a in quantity_list]
        max_stock = max(quantity_list_int)
    print(f"The shoe with highest stock is {quantity_dict[str(max_stock)]}, with {max_stock} remaining")
    print(f"{quantity_dict[str(max_stock)]} is now on sale!")
    pass


# ==========Main Menu=============
# Use function read_shoes_data to populate the shoe list, then ask the user to select an option. Depending on their
# selection, a function will be called. Once the function has run, the user will be returned to the main menu until 'e'
# is selected to break the loop
read_shoes_data()
while True:
    menu = input('''Select one of the following options below:
va  - View all shoe data stored in the inventory
a   - Add a new shoe to the inventory
r   - Check lowest stock (and add additional stock)
s   - Search for a shoe model by its code
v   - View the total value for each model of shoe
h   - Check the highest stock
e - Exit
: ''').lower()

    if menu == "va":
        view_all()

    elif menu == "a":
        capture_shoes()

    elif menu == "r":
        re_stock()

    elif menu == "s":
        search_shoe()

    elif menu == "v":
        value_per_item()

    elif menu == "h":
        highest_qty()

    elif menu == "e":
        print("Goodbye!")
        break

    else:
        print("Selection not recognised, please try again")
