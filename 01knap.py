def knapsack(weights,profits,capacity):
    steps=0
    n = len(weights)

    #create DP table
    dp = [[0 for _ in range(capacity+1)]for _ in range(n+1)]
    steps = n * capacity

    #Build Table from Bottom up manner

    for i in range(1,n+1):
        for w in range(1,capacity+1):
            steps +=1
            if weights[i-1] <= w:
                dp[i][w] = max(profits[i-1] + dp[i-1][w-weights[i-1]],dp[i-1][w])
            else:
                dp[i][w]=dp[i-1][w]

    print('Maximum Profit - ',dp[n][capacity])
    print('Steps - ',steps)

weights=[2,3,4,5]
profits = [3,4,5,6]
capacity=5

knapsack(weights,profits,capacity)