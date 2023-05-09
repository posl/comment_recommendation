def main():
    N = int(input())
    MOD = 10**9 + 7
    ans = (10**N - 2*(9**N) + 8**N) % MOD
    print(ans)
