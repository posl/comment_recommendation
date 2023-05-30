def solve(k):
    if k%2==0 or k%5==0:
        return -1
    else:
        i=1
        while True:
            if (10**i)%k==1:
                return i
            else:
                i+=1
k=int(input())
print(solve(k))
