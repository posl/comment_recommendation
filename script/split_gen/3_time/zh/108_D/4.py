def solve():
    L = int(input())
    N = 20
    M = 60
    print(N, M)
    for i in range(1, N):
        print(i, i+1, 0)
    for i in range(1, N-2):
        print(i, i+2, 10**6)
    print(1, 4, L-(N-2)*(10**6))
    for i in range(5, N+1):
        print(4, i, 10**5)
