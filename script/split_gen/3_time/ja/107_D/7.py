def solve():
    N = int(input())
    A = list(map(int,input().split()))
    B = [0]*N
    for i in range(N):
        if i == 0:
            B[i] = A[i]
        else:
            B[i] = A[i] + B[i-1]
    B.sort()
    if N % 2 == 0:
        print((B[int(N/2)]+B[int(N/2)-1])//2)
    else:
        print(B[int(N/2)])
