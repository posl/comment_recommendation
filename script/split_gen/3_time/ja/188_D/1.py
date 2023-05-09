def main():
    N, C = map(int, input().split())
    AB = []
    for i in range(N):
        a, b, c = map(int, input().split())
        AB.append((a, c))
        AB.append((b+1, -c))
    AB.sort(key=lambda x: x[0])
    ans = 0
    cnt = 0
    for i in range(len(AB)-1):
        cnt += AB[i][1]
        ans += min(cnt, C) * (AB[i+1][0] - AB[i][0])
    print(ans)
