SALES_TAX_RATE = 0.04
EXTRA_SAUCE_COST = 0.50

pizza_prices = {
    'small' : 7.00,
    's': 7.00,
    'medium' : 10.75,
    'm': 10.75,
    'large' : 14.75,
    'l': 14.75
}

topping_prices = {
    'small': 0.50,
    's': 0.50,
    'medium' : 1.00,
    'm': 1.00,
    'large': 1.50,
    'l': 1.50
}

subtotal = 0.0
count = 0
number_pizzas = int(input("How many pizzas? ").strip())

while number_pizzas > 0:
    count += 1
    print(f'Pizza Order: {count}')
    size_pizza = input('What size pizza would you like? (Small, Medium, Large):').strip().lower()
    num_toppings = int(input("How many toppings would you like?").strip())
    extra_sauce = input('Would you like extra sauce for $0.50? (Y/N)').strip().lower()
    temp_total = pizza_prices[size_pizza] + topping_prices[size_pizza] * num_toppings
    subtotal += temp_total

    order_description = f'A {size_pizza.capitalize()} pizza with {num_toppings} toppings'

    if extra_sauce in ('yes' or 'y'):
        temp_total += EXTRA_SAUCE_COST
        subtotal += EXTRA_SAUCE_COST
        order_description += f' and extra sauce'
    order_description += f' is ${temp_total:.2f}'

    print(order_description)
    number_pizzas -= 1

tax_amount = subtotal * SALES_TAX_RATE
total = subtotal + tax_amount

print(f'Subtotal:      ${subtotal:.2f}\n'
      f'Tax (4%):      ${tax_amount:.2f}\n'
      f'Total:         ${total:.2f}\n')
