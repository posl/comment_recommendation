def main():
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    mod = 10**9+7
    ans = 1
    for i in range(N):
        ans *= max(C[i]-i, 0)
        ans %= mod
    print(ans)
