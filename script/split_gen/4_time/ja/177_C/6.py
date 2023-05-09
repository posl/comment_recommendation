def main():
    N = int(input())
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0
    s = 0
    for i in range(N):
        s += A[i]
    for i in range(N):
        s -= A[i]
        ans += (A[i] * s)
        ans %= mod
    print(ans)
