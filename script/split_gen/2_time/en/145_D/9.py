def main():
    X,Y = map(int,input().split())
    if (X+Y) % 3 != 0:
        print(0)
        return
    n = (X+Y)//3
    if X > n or Y > n:
        print(0)
        return
    mod = 10**9+7
    ans = 1
    for i in range(n+1,n+X+1):
        ans *= i
        ans %= mod
    for i in range(1,X+1):
        ans *= pow(i,mod-2,mod)
        ans %= mod
    print(ans)
