def main():
    n, m, t = map(int, input().split())
    a = []
    b = []
    for _ in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.append(t)
    b.append(t)
    battery = n
    for i in range(m+1):
        battery -= a[i] - b[i-1]
        if battery <= 0:
            print('No')
            return
        battery += b[i] - a[i]
        battery = min(battery, n)
    print('Yes')
