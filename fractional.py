def fract(weights, profits, capacity):
    steps = 0
    n = len(weights)

    # Calculate profit/weight ratio
    ratio = [p / w for p, w in zip(profits, weights)]
    steps += n

    # Combine all data
    items = list(zip(weights, profits, ratio))
    steps += n

    # Sort by ratio (descending)
    items.sort(key=lambda x: x[2], reverse=True)
    steps += n

    total_profit = 0
    for w, p, r in items:
        steps += 1
        if capacity >= w:
            capacity -= w
            total_profit += p
            steps += 2
        else:
            total_profit += r * capacity
            steps += 1
            break

    print("\nMaximum Profit =", total_profit)
    print("Steps Count =", steps)


# ---------- User Input ----------
n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    w = float(input(f"Enter weight of item {i+1}: "))
    p = float(input(f"Enter profit of item {i+1}: "))
    weights.append(w)
    profits.append(p)

capacity = float(input("Enter knapsack capacity: "))

fract(weights, profits, capacity)


