prices = list(map(int, input("Enter prices separated by space: ").split()))

min_price = prices[0]
max_profit = 0

for price in prices:
    min_price = min(min_price, price)
    max_profit = max(max_profit, price - min_price)

print("Maximum Profit:", max_profit)
