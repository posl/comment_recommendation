def cabbage():
    n, a, x, y = input().split()
    n = int(n)
    a = int(a)
    x = int(x)
    y = int(y)
    if n > a:
        print(a*x + (n-a)*y)
    else:
        print(n*x)

if __name__ == '__main__':
    cabbage()