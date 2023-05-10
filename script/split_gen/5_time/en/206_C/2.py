def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1
    sum = 0
    for k in d:
        sum += d[k] * (d[k] - 1) // 2
    print(sum)
