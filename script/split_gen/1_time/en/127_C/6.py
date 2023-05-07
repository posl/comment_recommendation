def main():
    N, M = map(int, input().split())
    l = 0
    r = N + 1
    for i in range(M):
        L, R = map(int, input().split())
        if l < L:
            l = L
        if r > R:
            r = R
    print(r - l + 1 if r >= l else 0)
