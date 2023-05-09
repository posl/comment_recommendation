def main():
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s.append(10 ** 11)
    t.append(10 ** 11)
    for i in range(Q):
        ans = 10 ** 20
        a = bisect_left(s, x[i])
        b = bisect_left(t, x[i])
        for j in (a - 1, a):
            for k in (b - 1, b):
                d1 = abs(s[j] - x[i]) + abs(t[k] - s[j])
                d2 = abs(t[k] - x[i]) + abs(s[j] - t[k])
                ans = min(ans, d1, d2)
        print(ans)
