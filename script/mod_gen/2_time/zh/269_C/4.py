def solve():
    n = int(input())
    ans = []
    for i in range(1 << 15):
        s = 0
        for j in range(15):
            if (i >> j) & 1:
                s += 1 << j
        if s <= 60:
            ans.append(s)
    ans.sort()
    for i in ans:
        if i <= n:
            print(i)
solve()
