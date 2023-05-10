def f(h, a):
    return (h + a - 1) // a
h, a = map(int, input().split())
print(f(h, a))

if __name__ == '__main__':
    f()