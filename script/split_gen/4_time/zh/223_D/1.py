def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for i in range(M)]
    A = [0] * N
    B = [0] * N
    for i in range(M):
        A[AB[i][0]-1] += 1
        B[AB[i][1]-1] += 1
    if max(A) > 1 or max(B) > 1:
        print(-1)
    else:
        P = [0] * N
        for i in range(N):
            if A[i] == 0:
                P[0] = i + 1
        for i in range(N-1):
            for j in range(M):
                if P[i] == AB[j][0]:
                    P[i+1] = AB[j][1]
        for i in range(N):
            print(P[i], end=" ")
        print()
main()
