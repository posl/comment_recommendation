def check(a, b):
    if a == b:
        return False
    if a > b:
        a, b = b, a
    if a == 1 and b == N:
        return False
    if b - a == 1:
        return False
    return True
N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
