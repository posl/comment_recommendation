def get_input():
    n, s = map(int, input().split())
    ab = []
    for _ in range(n):
        ab.append(list(map(int, input().split())))
    return n, s, ab
