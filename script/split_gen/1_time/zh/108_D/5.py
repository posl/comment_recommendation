def build_graph(L):
    # L = 4
    # N = 8
    # M = 10
    N = L + 4
    M = L + 6
    print(N, M)
    for i in range(1, L + 1):
        print(i, i + 1, 0)
    for i in range(1, L + 2):
        print(i, i + 2, 1)
    for i in range(1, L + 3):
        print(i, i + 3, 0)
    print(L + 1, L + 3, 3)
    print(L + 3, L + 4, 1)
L = int(input())
build_graph(L)
