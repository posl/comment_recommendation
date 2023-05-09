def main():
    N = int(input())
    x = list(map(int, input().split()))
    res1 = 0
    res2 = 0
    res3 = 0
    for i in range(N):
        res1 += abs(x[i])
        res2 += x[i]**2
        res3 = max(res3, abs(x[i]))
    res2 = res2**0.5
    print(res1)
    print(res2)
    print(res3)
