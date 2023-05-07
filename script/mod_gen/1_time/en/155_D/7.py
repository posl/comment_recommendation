def check(n, k, a):
    b = sorted(a)
    c = []
    for i in range(n):
        for j in range(i + 1, n):
            c.append(b[i] * b[j])
    c = sorted(c)
    return c[k - 1]
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(check(n, k, a))

if __name__ == '__main__':
    check()