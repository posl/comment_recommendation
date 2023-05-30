def dice():
    N, K = map(int, input().split())
    p = list(map(int, input().split()))
    p.sort()
    max_sum = 0
    for i in range(N-K+1):
        sum = 0
        for j in range(K):
            sum += p[i+j]
        if sum > max_sum:
            max_sum = sum
    return max_sum/2
print(dice())
