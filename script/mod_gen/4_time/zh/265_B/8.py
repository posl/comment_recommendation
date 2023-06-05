def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))
    XY = [list(map(int, input().split())) for _ in range(M)]
    if A[0] > T:
        print("No")
        return
    for i in range(1, N):
        A[i] += A[i-1]
    for i in range(M):
        A[XY[i][0]-1] += XY[i][1]
    if A[-1] > T:
        print("No")
        return
    print("Yes")
    return

if __name__ == '__main__':
    solve()