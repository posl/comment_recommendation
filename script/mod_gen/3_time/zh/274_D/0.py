def check(n, x, y, a):
    for i in range(n):
        for j in range(i+1, n):
            if (a[i]-a[j])**2 == (x**2+y**2):
                return True
    return False
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
a.append(0)
a.append(0)

if __name__ == '__main__':
    check()