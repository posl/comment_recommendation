def main():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = []
    y = []
    for _ in range(m):
        x_, y_ = map(int, input().split())
        x.append(x_)
        y.append(y_)
    time = 0
    prev = 0
    for i in range(n):
        if i == 0:
            time = t
        else:
            time -= (a[i-1]-a[i-2])
        if time <= 0:
            print('No')
            return
        if i+1 in x:
            time += (y[x.index(i+1)] - prev)
            prev = y[x.index(i+1)]
        else:
            if prev != 0:
                time += (y[x.index(i+1)] - prev)
                prev = y[x.index(i+1)]
    if time - (a[-1]-a[-2]) <= 0:
        print('No')
    else:
        print('Yes')
