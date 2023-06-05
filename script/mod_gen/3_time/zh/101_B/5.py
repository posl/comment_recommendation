def S(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
N=int(input())
print('Yes' if N%S(N)==0 else 'No')
