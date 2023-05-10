def main():
    N, K = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(N)]
    AB.sort()
    ans = K
    for i in range(N):
        if ans < AB[i][0]:
            break
        ans += AB[i][1]
    print(ans)
