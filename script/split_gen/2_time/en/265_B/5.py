def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for i in range(m):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    time = t
    room = 1
    for i in range(n-1):
        time -= a[i]
        if time <= 0:
            print("No")
            return
        if room in x:
            time += y[x.index(room)]
        room += 1
    print("Yes")
    return
