def f(x):
    if x < 10:
        return x
    d = len(str(x))
    return x - 10**(d-1) + 1 + 9*(d-1)
N = int(input())
print((f(N) + sum(f(10**i-1) - f(10**(i-1)-1) for i in range(1, len(str(N)))) % 998244353))

if __name__ == '__main__':
    f()