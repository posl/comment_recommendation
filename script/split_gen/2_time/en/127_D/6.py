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
    c.sort(reverse=True)
    j = 0
    for i in range(n):
        if a[i] < c[j]:
            a[i] = c[j]
            j += 1
            if j == m:
                break
    print(sum(a))
