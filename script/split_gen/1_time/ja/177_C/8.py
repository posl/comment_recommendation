def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (A[i] * (i - N + 1 + i)) % (10 ** 9 + 7)
        ans %= (10 ** 9 + 7)
    print(ans)
