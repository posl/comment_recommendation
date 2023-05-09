def main():
    N = int(input())
    A = list(map(int,input().split()))
    Q = int(input())
    AC = [[0]*(N+1) for _ in range(N+1)]
    for i in range(N):
        AC[i+1][A[i]] = 1
    for i in range(N):
        for j in range(1,N+1):
            AC[i+1][j] += AC[i][j]
    for _ in range(Q):
        L,R,X = map(int,input().split())
        print(AC[R][X]-AC[L-1][X])
