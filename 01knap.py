def knapsack(weights, profits, capacity):
    steps = 0
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    steps = n * capacity

    # Build table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            steps += 1
            if weights[i - 1] <= w:
                dp[i][w] = max(profits[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    print("\nMaximum Profit =", dp[n][capacity])
    print("Steps Count =", steps)


# ---------- User Input ----------
n = int(input("Enter number of items: "))

weights = []
profits = []

for i in range(n):
    w = int(input(f"Enter weight of item {i + 1}: "))
    p = int(input(f"Enter profit of item {i + 1}: "))
    weights.append(w)
    profits.append(p)

capacity = int(input("Enter knapsack capacity: "))

knapsack(weights, profits, capacity)
