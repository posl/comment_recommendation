def main():
    N, K = map(int, input().split())
    sushi = [list(map(int, input().split())) for _ in range(N)]
    sushi.sort(key=lambda x: x[1], reverse=True)
    t = set()
    t_add = t.add
    t_discard = t.discard
    t_len = len
    t_clear = t.clear
    ans = 0
    for i in range(N):
        t_add(sushi[i][0])
        if t_len(t) >= K:
            ans = max(ans, sum([sushi[j][1] for j in range(i-K+1, i+1)]) + t_len(t)**2)
            t_clear()
            for j in range(i-K+1, i+1):
                t_add(sushi[j][0])
            if t_len(t) >= K:
                ans = max(ans, sum([sushi[j][1] for j in range(i-K+1, i+1)]) + t_len(t)**2)
            t_discard(sushi[i-K+1][0])
    print(ans)
