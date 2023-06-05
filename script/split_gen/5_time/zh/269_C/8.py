def f(n):
    if n==0:
        return [0]
    elif n==1:
        return [0,1]
    else:
        l=f(n-1)
        return l+[i+2**(n-1) for i in l[::-1]]
n=int(input())
print(*f(n),sep='\n')
