def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    for i in range(1<<n):
        b.append((a[i], i+1))
    b.sort()
    c = []
    for i in range(1<<n):
        c.append(b[i][1])
    d = []
    for i in range(1<<n):
        d.append(c[i])
    for i in range(n-1):
        e = []
        for j in range(1<<(n-i-1)):
            if d[2*j] > d[2*j+1]:
                e.append(d[2*j])
            else:
                e.append(d[2*j+1])
        for j in range(1<<(n-i-1)):
            d[j] = e[j]
    print(d[1])
