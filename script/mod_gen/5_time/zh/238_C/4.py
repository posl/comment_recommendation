def getSum(N):
    n = len(str(N))
    sum = 0
    for i in range(1,n):
        sum += i * 9 * (10 ** (i-1))
    sum += n * (N - 10 ** (n-1) + 1)
    return sum
N = int(input())
print(getSum(N) % 998244353)
