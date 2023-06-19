def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    bc = []
    for i in range(m):
        b, c = map(int, input().split())
        bc.append((b, c))
    a.sort()
    bc.sort(key=lambda x: x[1], reverse=True)
    i, j = 0, 0
    while i < n and j < m:
        if a[i] < bc[j][1]:
            a[i] = bc[j][1]
            bc[j] = (bc[j][0] - 1, bc[j][1])
            if bc[j][0] == 0:
                j += 1
        i += 1
    print(sum(a))
