def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    ans = -10**18
    for i in range(n):
        cur = i
        score = 0
        cnt = 0
        path = []
        while cnt < k:
            cur = p[cur]-1
            path.append(c[cur])
            score += c[cur]
            cnt += 1
            if cur == i:
                break
        if cnt == k:
            ans = max(ans, score)
            continue
        if score <= 0:
            ans = max(ans, max(path))
            continue
        loop = (k-cnt)//len(path)
        rest = (k-cnt)%len(path)
        ans = max(ans, max(path)*loop+max(0, score)*loop+max(path[:rest]))
    print(ans)
