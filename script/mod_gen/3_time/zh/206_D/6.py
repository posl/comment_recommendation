def solve():
    from collections import Counter
    n = int(input())
    a = list(map(int,input().split()))
    b = Counter(a)
    ans = 0
    for k,v in b.items():
        if k > v:
            ans += v
        elif k < v:
            ans += v-k
    print(ans)
solve()
