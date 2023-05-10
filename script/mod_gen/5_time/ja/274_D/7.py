def check(x, y, a):
    n = len(a)
    for i in range(n):
        for j in range(i+1, n):
            if (x - a[i])**2 + (y - a[j])**2 == a[i]**2 + a[j]**2:
                return True
    return False
n, x, y = map(int, input().split())
a = list(map(int, input().split()))

if __name__ == '__main__':
    check()