def getAns(a,b,k):
    count = 0
    while True:
        if a >= b:
            return count
        a *= k
        count += 1
a,b,k = map(int,input().split())
print(getAns(a,b,k))
