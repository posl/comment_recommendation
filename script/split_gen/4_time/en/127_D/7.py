def main():
    # get input
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = []
    c = []
    for i in range(m):
        b_i, c_i = map(int, input().split())
        b.append(b_i)
        c.append(c_i)
    # solve
    a.sort(reverse=True)
    b_c = list(zip(b, c))
    b_c.sort(key=lambda x: x[1], reverse=True)
    i = 0
    j = 0
    while i < n and j < m:
        if a[i] < b_c[j][1]:
            a[i] = b_c[j][1]
            b_c[j][0] -= 1
            if b_c[j][0] == 0:
                j += 1
        else:
            break
        i += 1
    # output
    print(sum(a))
