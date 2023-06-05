def f(k):
    if k%2==0 or k%5==0:
        return -1
    else:
        a=7
        for i in range(1,k+1):
            if a%k==0:
                return i
            else:
                a=a*10+7
k=int(input())
print(f(k))
