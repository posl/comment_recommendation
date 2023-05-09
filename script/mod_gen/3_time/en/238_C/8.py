def  main():
    N = int(input())
    MOD = 998244353
    ans = 0
    for i in range(1, 19):
        l = 10 ** (i - 1)
        r = min(10 ** i - 1, N)
        ans += (r - l + 1) * i
        ans %= MOD
    print(ans)

if __name__ == '__main__':
    ()