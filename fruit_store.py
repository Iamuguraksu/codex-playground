FRUIT_PRICES = {
    "apple": 1.00,
    "banana": 0.50,
    "orange": 0.80,
    "grape": 2.50,
    "mango": 1.50,
}

def main():
    print("Available fruits and prices:")
    for fruit, price in FRUIT_PRICES.items():
        print(f"{fruit}: ${price:.2f}")

    total = 0.0
    while True:
        choice = input("What fruit would you like to buy? (type 'done' to finish) ").strip().lower()
        if choice == 'done':
            break
        if choice not in FRUIT_PRICES:
            print("Sorry, that fruit is not available.")
            continue
        qty_input = input(f"How many {choice}s would you like? ").strip()
        try:
            qty = int(qty_input)
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue
        total += FRUIT_PRICES[choice] * qty
        print(f"Added {qty} {choice}(s) to your bill.")

    print(f"Your total bill is ${total:.2f}")

if __name__ == "__main__":
    main()
