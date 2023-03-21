# -*- coding: utf-8 -*-
"""
Description:

Write a program that allows the user to calculate the price of a pizza. A pizza has:

a base
a size
toppings

Assume the system stores everything in-memory, no storage is required.
"""

from pizza_prices_config import PIZZA_PRICES, PIZZA_TOPPINGS

def calculate_price(base, size, toppings):
    price = PIZZA_PRICES[base][size]
    for topping in toppings:
        if topping not in PIZZA_TOPPINGS:
            print(f"Invalid topping '{topping}' requested.")
            return None
        price += PIZZA_TOPPINGS[topping]
    return price

def get_number_of_pizzas():
    while True:
        try:
            num_pizzas = int(input("How many pizzas would you like to order? "))
            if num_pizzas > 0:
                return num_pizzas
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("Please enter a valid integer.")

def get_pizza_order(order_num):
    print(f"Enter details for pizza {order_num}:")
    base = input("Enter pizza base (Margherita, Pepperoni, Vegetarian): ").lower()
    while base not in PIZZA_PRICES:
        base = input("Please enter a valid pizza base (Margherita, Pepperoni, Vegetarian): ").lower()
    size = input("Enter pizza size (Small, Medium, Large): ").lower()
    while size not in PIZZA_PRICES[base]:
        size = input(f"Please enter a valid size for {base} pizza (Small, Medium, Large): ").lower()
    toppings = input("Enter pizza toppings (comma-separated): ").lower().split(",")
    price = calculate_price(base, size, toppings)
    while price is None:
        toppings = input("Enter valid pizza toppings (comma-separated): ").lower().split(",")
        price = calculate_price(base, size, toppings)
    return {"base": base, "size": size, "toppings": toppings, "price": price}

def get_order_details():
    num_pizzas = get_number_of_pizzas()
    pizzas = []
    for i in range(num_pizzas):
        pizzas.append(get_pizza_order(i + 1))
    return pizzas

def display_order_details(pizzas):
    total_price = 0
    print(f"\nYour order of {len(pizzas)} pizzas has been placed.")
    for i, pizza in enumerate(pizzas):
        print(f"Pizza {i + 1}: {pizza['base']} ({pizza['size']}), toppings: {', '.join(pizza['toppings'])}")
        total_price += pizza['price']
    print(f"Total price: ${total_price:.2f}")

if __name__ == '__main__':
    pizzas = get_order_details()
    display_order_details(pizzas)
