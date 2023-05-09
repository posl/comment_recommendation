def main():
    import sys
    input = sys.stdin.readline
    N, C = map(int, input().split())
    AB = []
    for i in range(N):
        a, b, c = map(int, input().split())
        AB.append((a, c))
        AB.append((b + 1, -c))
    AB.sort()
    ans = 0
    d = 0
    t = 0
    for a, b in AB:
        ans += min(C, d) * (a - t)
        d += b
        t = a
    print(ans)
