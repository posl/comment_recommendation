def check(c, r, w, h, k):
    count = 0
    for i in range(h):
        for j in range(w):
            if c[i][j] == '#' and (i in r or j in w):
                count += 1
    if count == k:
        return 1
    else:
        return 0
h, w, k = map(int, input().split())
c = [list(input()) for _ in range(h)]
ans = 0
for i in range(2 ** h):
    for j in range(2 ** w):
        row = []
        col = []
        for l in range(h):
            if (i >> l) & 1:
                row.append(l)
        for m in range(w):
            if (j >> m) & 1:
                col.append(m)
        ans += check(c, row, col, h, w, k)
print(ans)
Python3
