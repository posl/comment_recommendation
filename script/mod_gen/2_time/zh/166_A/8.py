def getFloor(A,B,N):
    max = 0
    for x in range(0, N+1):
        if (A*x/B)-A*(x/B) > max:
            max = (A*x/B)-A*(x/B)
    return max
A,B,N = input().split()
A = int(A)
B = int(B)
N = int(N)
print(getFloor(A,B,N))
