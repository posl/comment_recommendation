def main():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for i in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    t = [0] * (N + 1)
    ans = 0
    for i in range(K):
        t[sushi[i][0]] += 1
        ans += sushi[i][1]
    cnt = 0
    for i in range(1, N + 1):
        if t[i] > 0:
            cnt += 1
    ans += cnt * cnt
    for i in range(K, N):
        if t[sushi[i][0]] == 0:
            for j in range(1, N + 1):
                if t[j] > 0:
                    t[j] -= 1
                    break
            t[sushi[i][0]] += 1
            cnt += 1
            ans = ans - cnt * cnt + (cnt + 1) * (cnt + 1)
    print(ans)
