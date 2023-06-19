def Pascal(n):
    if n==0:
        return [1]
    elif n==1:
        return [1,1]
    else:
        return [1]+[Pascal(n-1)[i-1]+Pascal(n-1)[i] for i in range(1,n)]+[1]
n=int(input())
for i in range(n):
    print(*Pascal(i))
