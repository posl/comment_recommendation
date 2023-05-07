def main():
    N, M = map(int, input().split())
    A = [input() for _ in range(2*N)]
    R = [i for i in range(1, 2*N+1)]
    for i in range(M):
        for j in range(0, 2*N, 2):
            if A[R[j]-1][i] == A[R[j+1]-1][i]:
                continue
            elif A[R[j]-1][i] == 'G':
                if A[R[j+1]-1][i] == 'C':
                    R[j], R[j+1] = R[j+1], R[j]
            elif A[R[j]-1][i] == 'C':
                if A[R[j+1]-1][i] == 'P':
                    R[j], R[j+1] = R[j+1], R[j]
            elif A[R[j]-1][i] == 'P':
                if A[R[j+1]-1][i] == 'G':
                    R[j], R[j+1] = R[j+1], R[j]
    for i in range(2*N):
        print(R[i])
