def TwoSum(L1,T):
    D={}
    for i in range(0, len(L1)):
        diff=T-L1[i]
        if diff in D:
            return D[diff],i
        D[L1[i]]=i

n=int(input())
L1=list(map(int,input().split()))
T=int(input())

R=TwoSum(L1,T)
print(R[0],R[1])
