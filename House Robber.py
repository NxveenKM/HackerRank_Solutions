def Robbery(n, cash):
    if n == 0: return 0
    if n == 1: return cash[0]
    
    dp = [0] * n
    dp[0] = cash[0]
    dp[1] = max(cash[0], cash[1])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + cash[i])
    
    return dp[n-1]

n = int(input())
cash = list(map(int, input().split()))
print(Robbery(n, cash))
