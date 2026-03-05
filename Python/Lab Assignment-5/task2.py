
prices = tuple(map(int, input("Enter prices of sold items separated by space: ").split()))

print("Total number of items sold:", len(prices))

print("Price of cheapest item sold:", min(prices))

print("Price of costliest item sold:", max(prices))

print("Prices in ascending order:", tuple(sorted(prices)))

costliest = max(prices)
count = prices.count(costliest)

print("Number of costliest items sold:", count)