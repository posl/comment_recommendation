def main():
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = 0
    for i in range(M):
        if i < N:
            ans += AB[i][1]
        else:
            ans += 0
    print(ans)
