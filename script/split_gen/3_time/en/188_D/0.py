def main():
    N, C = map(int, input().split())
    AB = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        AB.append((a, c))
        AB.append((b + 1, -c))
    AB.sort()
    t = 0
    ans = 0
    for ab in AB:
        ans += min(C, t) * (ab[0] - t)
        t = ab[0]
        t += ab[1]
    print(ans)
