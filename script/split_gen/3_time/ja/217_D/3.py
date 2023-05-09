def main():
    N, Q = map(int, input().split())
    L = [N]
    for i in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            L.append(x)
        else:
            L.sort()
            print(L[bisect.bisect_left(L, x)] - L[bisect.bisect_left(L, x) - 1])
