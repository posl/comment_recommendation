def f(x):
    return x**3+x**2+x*x+x+1
n = int(input())
for i in range(n, 10**18):
    if f(i) >= n:
        print(i)
        break

if __name__ == '__main__':
    f()