def burger(n,x):
    if n == 0:
        return 0 if x <= 0 else 1
    elif x <= 1 + a[n - 1]:
        return burger(n - 1, x - 1)
    else:
        return p[n - 1] + 1 + burger(n - 1, x - 2 - a[n - 1])
n, x = map(int,input().split())
p, a = [1], [1]
for i in range(n):
    p.append(2 * p[i] + 1)
    a.append(2 * a[i] + 3)
print(burger(n, x))

if __name__ == '__main__':
    burger()