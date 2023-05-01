def coin_exchange(coins, amount):
    n = len(coins)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(n):
        for j in range(coins[i], amount + 1):
            dp[j] = min(dp[j], dp[j - coins[i]] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1