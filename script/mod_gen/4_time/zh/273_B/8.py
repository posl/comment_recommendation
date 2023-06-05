def round_off(x,k):
    if k == 0:
        return x
    else:
        return round_off(x//10,k-1)*10**k if x%10**k >= 5*10**(k-1) else round_off(x//10,k-1)*10**k+5*10**(k-1)
x,k = map(int,input().split())
print(round_off(x,k))
