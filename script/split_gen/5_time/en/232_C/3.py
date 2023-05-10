def solve():
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
    for i in range(1, N+1):
        for j in range(1, N+1):
            if (i in A and j in B) or (i in B and j in A):
                if (i in C and j in D) or (i in D and j in C):
                    continue
                else:
                    print('No')
                    exit()
            else:
                if (i in C and j in D) or (i in D and j in C):
                    print('No')
                    exit()
                else:
                    continue
    print('Yes')
