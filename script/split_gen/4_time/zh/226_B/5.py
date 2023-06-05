def input():
    n = int(input())
    A = []
    for i in range(n):
        A.append(list(map(int, input().split())))
    return n, A
