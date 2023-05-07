def main():
    N, Q = map(int, input().split())
    A = [list(map(int, input().split())) for i in range(N)]
    B = [list(map(int, input().split())) for i in range(Q)]
    for i in range(Q):
        print(A[B[i][0] - 1][B[i][1] - 1])
