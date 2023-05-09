def main():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    D = []
    for i in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for i in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(N):
                for l in range(k + 1, N):
                    flag = 0
                    for m in range(M):
                        if (A[m] == i + 1 and B[m] == j + 1 and C[m] == k + 1 and D[m] == l + 1) or (A[m] == j + 1 and B[m] == i + 1 and C[m] == l + 1 and D[m] == k + 1):
                            flag = 1
                    if flag == 0:
                        print('No')
                        return
    print('Yes')
