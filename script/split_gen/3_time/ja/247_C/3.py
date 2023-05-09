def s(n):
    if n==1:
        return [1]
    else:
        return s(n-1)+[n]+s(n-1)
n=int(input())
print(' '.join(map(str,s(n))))
