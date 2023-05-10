def main():
    n,a,b = map(int,input().split())
    MOD = 10**9 + 7
    ans = pow(2,n,MOD) - 1
    for i in range(b):
        ans = ans * (n-i) % MOD
    for i in range(b):
        ans = ans * pow(i+1,MOD-2,MOD) % MOD
    for i in range(a):
        ans = ans * (n-i) % MOD
    for i in range(a):
        ans = ans * pow(i+1,MOD-2,MOD) % MOD
    print(ans)
