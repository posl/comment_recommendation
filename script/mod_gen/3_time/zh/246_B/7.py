def f(x, y):
    c = (x**2 + y**2)**0.5
    return x/c, y/c
a, b = map(int, input().split())
x, y = f(a, b)
print(x, y)

if __name__ == '__main__':
    f()