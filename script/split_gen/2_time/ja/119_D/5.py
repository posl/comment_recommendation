def main():
    import bisect
    A, B, Q = map(int, input().split())
    s = [int(input()) for _ in range(A)]
    t = [int(input()) for _ in range(B)]
    x = [int(input()) for _ in range(Q)]
    s.append(float('inf'))
    t.append(float('inf'))
    for i in range(Q):
        ans = float('inf')
        d = x[i]
        j = bisect.bisect_right(s, d)
        k = bisect.bisect_right(t, d)
        for a in [s[j-1], s[j]]:
            for b in [t[k-1], t[k]]:
                ans = min(ans, abs(d-a)+abs(a-b), abs(d-b)+abs(b-a))
        print(ans)
