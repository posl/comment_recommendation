def main():
    X, Y = map(int, input().split())
    mod = 10**9 + 7
    if (X+Y)%3 != 0:
        print(0)
        exit()
    n = (X+Y)//3
    m = min(X, Y)
    if n > m:
        print(0)
        exit()
    ans = 1
    for i in range(n):
        ans *= (m-i)
        ans %= mod
    for i in range(1, n+1):
        ans *= pow(i, mod-2, mod)
        ans %= mod
    print(ans)
