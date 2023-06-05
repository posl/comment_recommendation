def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    b = []
    c = []
    for i in range(m):
        b_i, c_i = map(int, input().split())
        b.append(b_i)
        c.append(c_i)
    b.sort()
    b.reverse()
    c.sort()
    c.reverse()
    sum = 0
    for i in range(n):
        if len(b) == 0:
            break
        if a[i] >= c[0]:
            sum += a[i]
        else:
            sum += c[0]
            b[0] -= 1
            if b[0] == 0:
                b.pop(0)
                c.pop(0)
    print(sum)
main()
