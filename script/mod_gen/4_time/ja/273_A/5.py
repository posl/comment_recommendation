def f(x):
    if x == 0:
        return 1
    return x * f(x - 1)
n = int(input())
print(f(n))

if __name__ == '__main__':
    f()