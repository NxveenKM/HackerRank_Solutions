def Coin_change(coins, t):
    coins.sort(reverse=True)
    sum = 0
    if t == 0: 
        return 0
    
    for i in coins:
        if t >= i:
            sum = sum + t // i
            t = t % i
    
    return sum if t == 0 else -1

n = int(input())
coins = list(map(int, input().strip().split()))
t = int(input())
print(Coin_change(coins, t))
