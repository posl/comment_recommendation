def solve():
    L = int(input())
    N = 1
    M = 0
    while N*(N-1)//2 <= L:
        N += 1
    N -= 1
    M = N*(N-1)//2
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N):
        for j in range(i+2, N+1):
            if M < L:
                print(i, j, M)
                M += 1
            else:
                print(i, j, 1)
solve()
