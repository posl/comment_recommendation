def main():
    N = int(input())
    MOD = 10**9 + 7
    ans = 0
    for i in range(1,N+1):
        ans += pow(10,i,MOD) - pow(9,i,MOD) - pow(9,i,MOD) + pow(8,i,MOD)
        ans %= MOD
    print(ans)
