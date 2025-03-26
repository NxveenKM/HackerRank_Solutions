def Max_SubArray(L1):
    Sum=L1[0]
    Curr=L1[0]

    for i in range (1,len(L1)):
        Curr = max(Curr+L1[i],L1[i])
        Sum = max(Curr,Sum)

    return Sum

n=int(input())
L1=list(map(int,input().split()))
print(Max_SubArray(L1))
