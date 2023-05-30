def solve(n):
    count=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i*j)**0.5==int((i*j)**0.5):
                count+=1
    return count
print(solve(int(input())))
