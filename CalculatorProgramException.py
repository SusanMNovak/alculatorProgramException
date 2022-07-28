# IS 280 Python Assignment 8 CalculatorProgramException Susan Novak

# !/usr/bin/env python3

# get_price function obtains a valid price and converts it to a float
def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")

# get_quantity function obtains a valid quantity and converts it to an integer
def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")

# main function takes the valid data from get_price and get_quantity, calculates and displays results
def main():
    print("The Total Calculator program\n")

    # get the price and quantity
    price = get_price()
    quantity = get_quantity()

    # calculate the total
    total = price * quantity

    # display the results
    print()
    print("PRICE:    ", price)
    print("QUANTITY: ", quantity)
    print("TOTAL:    ", total)


if __name__ == "__main__":
    main()
