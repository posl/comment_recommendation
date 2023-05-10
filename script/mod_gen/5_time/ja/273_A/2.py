def f(x):
    return x * f(x-1) if x > 0 else 1
n = int(input())
print(f(n))

if __name__ == '__main__':
    f()