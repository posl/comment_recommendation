def get_input():
    N = int(input())
    mountain = []
    for i in range(N):
        mountain.append(input().split())
    return N, mountain
