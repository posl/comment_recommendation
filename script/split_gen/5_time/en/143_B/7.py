def sum_takoyaki(N, d):
    sum = 0
    for i in range(N):
        for j in range(i+1, N):
            sum = sum + d[i]*d[j]
    return sum
N = int(input())
d = list(map(int, input().split()))
print(sum_takoyaki(N, d))
