def josephus(n, k):
    if n == 1:
        return 0
    else:
        return (josephus(n - 1, k) + k) % n

n = int(input().strip())
k = int(input().strip())
position = josephus(n, k) + 1
print(position)
