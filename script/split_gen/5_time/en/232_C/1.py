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
    if M == 0:
        print('Yes')
        exit()
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                continue
            else:
                tmp = 0
                for k in range(M):
                    if (A[k] == i and B[k] == j) or (A[k] == j and B[k] == i):
                        tmp += 1
                if tmp == 0:
                    print('No')
                    exit()
                else:
                    continue
    print('Yes')
    exit()
