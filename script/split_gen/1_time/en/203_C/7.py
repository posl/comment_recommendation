def main():
    N, K = map(int, input().split())
    friends = [list(map(int, input().split())) for _ in range(N)]
    friends.sort(key=lambda x: x[0])
    ans = 0
    for i in range(N):
        if K >= friends[i][0] - ans:
            K -= friends[i][0] - ans
            K += friends[i][1]
            ans = friends[i][0]
        else:
            ans += K
            K = 0
            break
    if K > 0:
        ans += K
    print(ans)
