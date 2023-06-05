def problem273_b():
    x,k = map(int,input().split())
    print(x//10**k*10**k+10**k) if x%10**k>=5*10**(k-1) else print(x//10**k*10**k)
