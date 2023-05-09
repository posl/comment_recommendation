def main():
    mod = 10**9 + 7
    N = int(input())
    ans = (10**N - 2*(9**N) + 8**N) % mod
    print(ans)
