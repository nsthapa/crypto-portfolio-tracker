print("Crypto Portfolio Tracker")

total_value = 0
num_coins = int(input("How many different cryptocurrencies do you own? "))
cryptos = []

for i in range(num_coins):
    print(f"\nCrypto {i + 1}")
    name = input("Enter crypto name (e.g. Bitcoin): ")
    amount = float(input("Enter amount owned: "))
    price = float(input("Enter current price in USD: "))

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
