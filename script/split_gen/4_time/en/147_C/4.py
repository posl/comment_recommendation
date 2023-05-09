def get_input():
    N = int(input())
    A = []
    xy = []
    for i in range(N):
        A.append(int(input()))
        xy.append([])
        for j in range(A[i]):
            xy[i].append(list(map(int, input().split())))
    return N, A, xy
