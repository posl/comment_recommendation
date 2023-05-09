def solution():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    sum_a = [0 for _ in range(n+1)]
    for i in range(n):
        sum_a[i+1] = sum_a[i] + a[i]
    from collections import Counter
    cnt = Counter()
    for i in range(n+1):
        cnt[sum_a[i]%m] += 1
    ans = 0
    for v in cnt.values():
        ans += v*(v-1)//2
    print(ans)
