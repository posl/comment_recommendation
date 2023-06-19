def f(n, m, a):
    b = []
    for j in range(m):
        count = 0
        for i in range(n):
            if a[i][j] == '#':
                count += 1
        b.append(count)
    return b
n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(input()))
b = f(n, m, a)
print(*b)

if __name__ == '__main__':
    f()