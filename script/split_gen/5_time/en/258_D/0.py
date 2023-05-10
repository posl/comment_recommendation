def main():
    N, X = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for i in range(N):
        ans += AB[i][0] * AB[i][1]
    ans += min([AB[i][1] for i in range(N)])
    ans *= X
    print(ans)
