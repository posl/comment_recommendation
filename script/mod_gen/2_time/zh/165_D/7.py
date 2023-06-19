def f(A,B,N):
    max = 0
    for x in range(N+1):
        if max < int(A*x/B) - A*int(x/B):
            max = int(A*x/B) - A*int(x/B)
    return max
A,B,N = map(int,input().split())
print(f(A,B,N))
