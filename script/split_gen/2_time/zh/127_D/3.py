def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(m):
        b_i, c_i = map(int, input().split())
        b.append(b_i)
        c.append(c_i)
    a.sort()
    a.reverse()
    a_i = 0
    c_i = 0
    while a_i < n and c_i < m:
        if a[a_i] >= c[c_i]:
            a_i += 1
        else:
            a[a_i] = c[c_i]
            b[c_i] -= 1
            if b[c_i] == 0:
                c_i += 1
    print(sum(a))
