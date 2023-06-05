def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        a0, b0 = map(int, input().split())
        a.append(a0)
        b.append(b0)
    c = [0 for i in range(n)]
    for i in range(n-1):
        c0 = c[a[i]-1]
        if c0 == 0:
            c0 = c[b[i]-1]
        elif c0 == c[b[i]-1]:
            c0 += 1
        c[a[i]-1] = c0
        c[b[i]-1] = c0
    print(max(c))
    for i in range(n-1):
        print(c[a[i]-1])
