def get_input():
    N = int(input())
    l = []
    for i in range(N):
        l.append(list(map(int, input().split())))
    return N, l
