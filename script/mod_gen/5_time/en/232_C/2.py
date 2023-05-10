def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    D = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    for i in range(M):
        C[i], D[i] = map(int, input().split())
    ans = "No"
    for i in range(2 ** N):
        P = []
        for j in range(N):
            if ((i >> j) & 1) == 1:
                P.append(j + 1)
        if len(P) != N:
            continue
        for j in range(M):
            if A[j] in P and B[j] in P:
                continue
            elif A[j] in P or B[j] in P:
                break
        else:
            for j in range(M):
                if C[j] in P and D[j] in P:
                    continue
                elif C[j] in P or D[j] in P:
                    break
            else:
                ans = "Yes"
                break
    print(ans)

if __name__ == '__main__':
    solve()