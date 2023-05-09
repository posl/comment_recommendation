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
    for i in range(1,N+1):
        for j in range(1,N+1):
            if i == j:
                continue
            if (i in A and j in A) or (i in B and j in B):
                if (i in C and j in C) or (i in D and j in D):
                    continue
                else:
                    print("No")
                    return
            else:
                if (i in C and j in C) or (i in D and j in D):
                    print("No")
                    return
                else:
                    continue
    print("Yes")

if __name__ == '__main__':
    solve()