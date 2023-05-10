def get_input():
    N = int(input())
    trampolines = []
    for _ in range(N):
        x, y, p = map(int, input().split())
        trampolines.append((x, y, p))
    return trampolines
