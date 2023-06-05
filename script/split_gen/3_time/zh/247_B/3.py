def get_input():
    N = int(input())
    names = []
    for i in range(N):
        names.append(input().split())
    return N, names
