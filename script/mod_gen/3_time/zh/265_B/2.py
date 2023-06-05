def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    A.append(0)
    A.insert(0,0)
    XY.sort()
    #print(A)
    #print(XY)
    for i in range(M):
        XY[i][0] += 1
    #print(XY)
    for i in range(M):
        A[XY[i][0]] += XY[i][1]
    #print(A)
    for i in range(1,N+1):
        A[i] += A[i-1]
    #print(A)
    for i in range(N):
        if A[i+1] - A[i] > A[i+1] - A[i-1]:
            A[i] = A[i+1]
    #print(A)
    if A[N] <= T:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    solve()