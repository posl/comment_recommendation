def calc(n, a, b):
    s = 0
    for i in range(n):
        s += a[i] / b[i]
    s /= 2
    t = 0
    for i in range(n):
        t += a[i] / b[i]
        if t >= s:
            return t
    return s
n = int(input())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i] = map(int, input().split())
print(calc(n, a, b))

if __name__ == '__main__':
    calc()