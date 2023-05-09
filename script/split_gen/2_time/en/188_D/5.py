def main():
    N, C = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        a = AB[i][0]
        b = AB[i][1]
        c = AB[i][2]
        ans += min(C, c) * (b - a + 1)
    print(ans)
