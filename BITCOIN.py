print("Crypto Portfolio Tracker")

total_value = 0

# asking how many coins, and catch letters typed instead of a number
while True:
    try:
        num_coins = int(input("How many different cryptocurrencies do you own? "))
    except ValueError:
        print("Please enter a whole number, not letters.")
        continue
    if num_coins <= 0:
        print("Please enter a number greater than 0.")
    elif num_coins > 20:
        print("Please enter 20 or fewer coins.")
    else:
        break

cryptos = []

for i in range(num_coins):
    print(f"\nCrypto {i + 1}")

    # asking for the coin name, and ask again if it is left blank
    while True:
        name = input("Enter crypto name (e.g. Bitcoin): ")
        if name.strip() == "":
            print("Crypto name cannot be blank. Try again.")
        else:
            break

    # asking for amount owned, catch letters and reject negative numbers
    while True:
        try:
            amount = float(input("Enter amount owned: "))
        except ValueError:
            print("Please enter a number, not letters.")
            continue
        if amount < 0:
            print("Amount cannot be negative.")
        else:
            break

    # ask for price, catch letters and reject negative numbers
    while True:
        try:
            price = float(input("Enter current price in USD: "))
        except ValueError:
            print("Please enter a number, not letters.")
            continue
        if price < 0:
            print("Price cannot be negative.")
        else:
            break

    value = amount * price
    total_value += value

    cryptos.append((name, amount, value))

print("\n---------------------------")
print("Crypto Portfolio Table:")
print(f"{'Crypto Name':<15} | {'Amount Owned':<15} | {'Value (USD)':<15}")
print("-" * 55)
for name, amount, value in cryptos:
    print(f"{name:<15} | {amount:<15} | ${value:.2f}")
print("-" * 55)
print(f"{'Total Portfolio':<30} | ${total_value:.2f}")

# short message based on how big the total portfolio value is
if total_value == 0:
    print("Your portfolio has no value yet.")
elif total_value < 1000:
    print("You have a small portfolio.")
else:
    print("You have a large portfolio!")
