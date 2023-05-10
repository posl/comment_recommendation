def problems185_b():
    n, m, t = map(int, input().split())
    bat = n
    a = 0
    for i in range(m):
        s, e = map(int, input().split())
        bat -= s - a
        if bat <= 0:
            print("No")
            return
        bat = min(n, bat + e - s)
        a = e
    bat -= t - a
    if bat <= 0:
        print("No")
        return
    print("Yes")
