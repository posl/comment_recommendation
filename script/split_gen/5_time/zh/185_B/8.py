def main():
    n, m, t = [int(x) for x in input().split()]
    a = []
    b = []
    for i in range(m):
        ai, bi = [int(x) for x in input().split()]
        a.append(ai)
        b.append(bi)
    a.append(t)
    b.append(t)
    ans = 'Yes'
    now = n
    for i in range(m + 1):
        now -= a[i] - b[i - 1]
        if now <= 0:
            ans = 'No'
            break
        now += b[i] - a[i]
        if now > n:
            now = n
    print(ans)
