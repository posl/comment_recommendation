def main():
    n, m, t = map(int, input().split())
    a = []
    b = []
    for _ in range(m):
        tmp = list(map(int, input().split()))
        a.append(tmp[0])
        b.append(tmp[1])
    n -= a[0]
    for i in range(m):
        if i == 0:
            n += b[i] - a[i]
        else:
            n += b[i] - a[i-1]
            if n > 100:
                n = 100
        if n <= 0:
            print("No")
            return
    n -= t - b[-1]
    if n <= 0:
        print("No")
        return
    print("Yes")
    return
