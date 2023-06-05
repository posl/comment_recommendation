def solve():
    n, m, t = map(int, input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    a.append(t)
    b.append(t)
    ans = 'No'
    for i in range(m + 1):
        if i == 0:
            if a[i] > 0:
                ans = 'Yes'
                break
        else:
            if a[i] - b[i - 1] > 0:
                ans = 'Yes'
                break
    print(ans)
