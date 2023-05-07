def main():
    N, C = map(int, input().split())
    AB = []
    for _ in range(N):
        a, b, c = map(int, input().split())
        AB.append((a, c))
        AB.append((b+1, -c))
    AB.sort()
    ans = 0
    now = 0
    for i in range(len(AB)-1):
        now += AB[i][1]
        ans += min(now, C) * (AB[i+1][0] - AB[i][0])
    print(ans)
