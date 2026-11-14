# Shopping Bill using Different Types of Arguments

# Positional Arguments
def calculate_bill(price, quantity):
    return price * quantity


# Keyword Arguments
def customer_details(name, city):
    print("Customer Name:", name)
    print("City:", city)


# Default Argument
def discount(amount, discount_percent=10):
    discount_amount = amount * discount_percent / 100
    final_amount = amount - discount_amount

    return discount_amount, final_amount


# Variable-Length Arguments
def calculate_items_total(*amounts):
    total = 0

    for amount in amounts:
        total += amount

    return total
    
# Main Program
customer = input("Enter customer name: ")
city = input("Enter city: ")

price1 = float(input("Enter price of Item 1: "))
qty1 = int(input("Enter quantity of Item 1: "))

price2 = float(input("Enter price of Item 2: "))
qty2 = int(input("Enter quantity of Item 2: "))

price3 = float(input("Enter price of Item 3: "))
qty3 = int(input("Enter quantity of Item 3: "))

# Positional Arguments
amount1 = calculate_bill(price1, qty1)
amount2 = calculate_bill(price2, qty2)
amount3 = calculate_bill(price3, qty3)

# Variable-length Arguments
total = calculate_items_total(amount1, amount2, amount3)

# Default Argument
discount_amount, final_amount = discount(total)

# Keyword Arguments
customer_details(name=customer, city=city)

print("----- SHOPPING BILL -----")
print("Item 1 Amount:", amount1)
print("Item 2 Amount:", amount2)
print("Item 3 Amount:", amount3)
print("Total Amount:", total)
print("Discount:", discount_amount)
print("Final Amount:", final_amount)
