def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        score = 0
        cnt = 0
        now = i
        while True:
            now = p[now] - 1
            score += c[now]
            cnt += 1
            if now == i:
                break
        #print(score, cnt)
        if score > 0:
            ans = max(ans, score * (k // cnt))
            if k % cnt != 0:
                ans = max(ans, score * (k // cnt - 1) + max(0, score))
        else:
            ans = max(ans, score)
    print(ans)
