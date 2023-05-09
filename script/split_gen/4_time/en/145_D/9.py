def main():
    #input
    X, Y = map(int,input().split())
    #solve
    if (X+Y)%3!=0:
        print(0)
        return
    a = (X+Y)//3
    b = Y-a
    if a<0 or b<0:
        print(0)
        return
    mod = 10**9+7
    ans = 1
    for i in range(a):
        ans = ans*(a+b-i)*pow(i+1,mod-2,mod)%mod
    print(ans)
