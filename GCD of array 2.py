def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def GCD(L1):
    current_gcd = L1[0]
    for num in L1[1:]:
        current_gcd = gcd(current_gcd, num)
    return current_gcd

n=int(input())
L1=list(map(int,input().split()))
print(GCD(L1))
