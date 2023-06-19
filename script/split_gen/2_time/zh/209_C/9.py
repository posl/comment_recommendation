def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    mod = 10**9+7
    ans = 1
    for i in range(n):
        ans *= max(0, c[i]-i)
        ans %= mod
    print(ans)
