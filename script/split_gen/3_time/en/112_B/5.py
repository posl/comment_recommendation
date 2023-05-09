def main():
    N, T = map(int, input().split())
    c = []
    t = []
    for _ in range(N):
        _c, _t = map(int, input().split())
        c.append(_c)
        t.append(_t)
    ans = 1001
    for i in range(N):
        if t[i] <= T:
            ans = min(ans, c[i])
    if ans == 1001:
        print("TLE")
    else:
        print(ans)
