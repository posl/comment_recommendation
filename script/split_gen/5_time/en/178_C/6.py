def main():
    n = int(input())
    #print(n)
    mod = 10**9 + 7
    #print(mod)
    ans = pow(10,n,mod) - 2*pow(9,n,mod) + pow(8,n,mod)
    #print(ans)
    print(ans%mod)
