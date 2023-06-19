def S(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s
k=int(input())
n=1
while k>0:
    if n%S(n)==0:
        print(n)
        k-=1
    n+=1
