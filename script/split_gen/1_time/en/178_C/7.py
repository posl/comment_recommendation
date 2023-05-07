def main():
    n = int(input())
    mod = 10**9 + 7
    ans = 0
    for i in range(1,n+1):
        ans += (10**i - 9**i - 9**i + 8**i)
    print(ans%mod)
