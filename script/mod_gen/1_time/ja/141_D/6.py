def calc(n, m, a):
    a.sort(reverse=True)
    for i in range(m):
        a[0] = a[0] // 2
        a.sort(reverse=True)
    return sum(a)
n, m = map(int, input().split())
a = list(map(int, input().split()))
print(calc(n, m, a))

if __name__ == '__main__':
    calc()