def Stock(L1):
    if len(L1) < 2:
        return 0

    max_profit = 0
    min_price = L1[0]

    for price in L1:
        if price < min_price:
            min_price = price
        profit = price - min_price
        if profit > max_profit:
            max_profit = profit

    return max_profit
            
n=int(input())
L1=L1=list(map(int,input().split()))
print(Stock(L1))
