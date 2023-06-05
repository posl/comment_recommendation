def solve():
    n, k = map(int, input().split())
    td = [list(map(int, input().split())) for _ in range(n)]
    td.sort(key=lambda x: -x[1])
    td.sort(key=lambda x: x[0])
    td.append([0, 0])
    i = 0
    j = 0
    s = 0
    t = []
    while i < n:
        while j < n and td[i][0] == td[j][0]:
            t.append(td[j][1])
            j += 1
        t.sort(reverse=True)
        for l in range(len(t)):
            if l < k - i:
                s += t[l]
            else:
                break
        i = j
        t = []
    print(s)
solve()
