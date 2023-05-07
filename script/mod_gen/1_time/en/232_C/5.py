def solve():
    N, M = map(int, input().split())
    A, B = [], []
    C, D = [], []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    for _ in range(M):
        c, d = map(int, input().split())
        C.append(c)
        D.append(d)
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            flag = True
            for k in range(M):
                if (i in [A[k], B[k]]) and (j in [A[k], B[k]]):
                    if not ((i in [C[k], D[k]]) and (j in [C[k], D[k]])):
                        flag = False
                        break
                if (i in [C[k], D[k]]) and (j in [C[k], D[k]]):
                    if not ((i in [A[k], B[k]]) and (j in [A[k], B[k]])):
                        flag = False
                        break
            if not flag:
                break
        if not flag:
            break
    if flag:
        print('Yes')
    else:
        print('No')
solve()
N, M = map(int, input().split())
A, B = [], []
C, D = [], []
for _ in range(M):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
for _ in range(M):
    c, d = map(int, input().split())
    C.append(c)
    D.append(d)
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        flag = True
        for k in range(M):
            if (i in [A[k], B[k]]) and (j in [A[k], B[k]]):
                if not ((i in [C[k], D[k]]) and (j in [C[k], D[k]])):
                    flag = False
                    break
            if (i in [C[k], D[k]]) and (j in [C[k], D[k]]):
                if not ((i in [A[k], B[k]]) and (j in [A[k], B[k]])):

if __name__ == '__main__':
    solve()