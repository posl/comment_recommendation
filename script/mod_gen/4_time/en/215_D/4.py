def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
a = list(set(a))
min = 1
max = m

if __name__ == '__main__':
    gcd()