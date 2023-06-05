def get_input():
    N = int(input())
    x = []
    y = []
    for i in range(N):
        x.append(int(input().split()[0]))
        y.append(int(input().split()[1]))
    return N, x, y
