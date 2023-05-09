def main():
    N = int(input())
    ans = 0
    for i in range(1, 19):
        ans += min(10**i-1, N) - 10**(i-1) + 1
    print(ans % 998244353)
