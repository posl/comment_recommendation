def main():
    n = int(input())
    mod = 10**9+7
    ans = 10**n - 2*(9**n) + 8**n
    print(ans%mod)
