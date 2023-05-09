def main():
    n,k = map(int,input().split())
    mod = 10**9+7
    for i in range(1,k+1):
        a = n-k+1
        b = k-i
        c = i-1
        print((a*(a+b+c)//2)%mod)
