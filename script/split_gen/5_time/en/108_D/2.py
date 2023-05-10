def solve():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N-2):
        if (L >> i) & 1:
            print(i, i+2, 1 << i)
    if L == 3:
        print(1, 3, 2)
