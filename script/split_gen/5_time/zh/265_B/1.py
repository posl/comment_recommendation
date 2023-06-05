def solve():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    xy = []
    for i in range(m):
        xy.append(list(map(int, input().split())))
    time = t
    for i in range(n-1):
        time -= a[i]
        if i+1 in [x[0] for x in xy]:
            time += [x[1] for x in xy if x[0] == i+1][0]
        if time <= 0:
            print("No")
            return
    print("Yes")
