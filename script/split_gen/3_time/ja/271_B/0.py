def main():
    N, Q = map(int, input().split())
    A = []
    for i in range(N):
        A.append(list(map(int, input().split())))
    B = []
    for i in range(Q):
        B.append(list(map(int, input().split())))
    for i in range(Q):
        print(A[B[i][0]-1][B[i][1]-1])
