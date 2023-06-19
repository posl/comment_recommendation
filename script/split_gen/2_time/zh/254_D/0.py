def solve(n):
    count=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i*j==int(i**0.5)**2*j:
                count+=1
    print(count)
