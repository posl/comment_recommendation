def problems265_b():
    n, m, t = map(int, input().split())
    a = list(map(int, input().split()))
    x = [0] * m
    y = [0] * m
    for i in range(m):
        x[i], y[i] = map(int, input().split())
    for i in range(n-1):
        t = t - a[i]
        if t <= 0:
            print("No")
            return
        for j in range(m):
            if x[j] == i+1:
                t = t + y[j]
                if t > 0:
                    break
    t = t - a[n-1]
    if t > 0:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    problems265_b()