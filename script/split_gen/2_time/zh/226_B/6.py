def readinput():
    n = int(input())
    L = []
    for i in range(n):
        l = list(map(int, input().split()))
        L.append(l)
    return n, L
