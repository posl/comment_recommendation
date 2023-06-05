def solve():
    N,M,T = map(int,input().split())
    A = list(map(int,input().split()))
    XY = [list(map(int,input().split())) for _ in range(M)]
    #print(N,M,T)
    #print(A)
    #print(XY)
    for i in range(N-1):
        if T <= A[i]:
            return False
        T -= A[i]
        for j in range(M):
            if XY[j][0] == i+2:
                T += XY[j][1]
                break
    return True

if __name__ == '__main__':
    solve()