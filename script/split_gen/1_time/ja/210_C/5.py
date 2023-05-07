def main():
    n,k = map(int,input().split())
    c = list(map(int,input().split()))
    ans = 0
    cnt = {}
    for i in range(n):
        if i >= k:
            cnt[c[i-k]] -= 1
            if cnt[c[i-k]] == 0:
                del cnt[c[i-k]]
        if c[i] not in cnt:
            cnt[c[i]] = 0
        cnt[c[i]] += 1
        ans = max(ans,len(cnt))
    print(ans)
