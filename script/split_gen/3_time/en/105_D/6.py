def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    summod = [0] * (N + 1)
    for i in range(N):
        summod[i + 1] = (summod[i] + A[i]) % M
    ans = 0
    for i in range(N + 1):
        ans += summod[:i].count(summod[i])
    print(ans)
