def solve():
    n = int(input())
    d = {}
    for _ in range(n):
        s = input()
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    max_cnt = max(d.values())
    ans = []
    for k in d:
        if d[k] == max_cnt:
            ans.append(k)
    ans.sort()
    for s in ans:
        print(s)
solve()
