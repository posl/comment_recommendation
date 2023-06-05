def f(m):
    global n
    global a
    res = 0
    for i in range(n):
        res += m % a[i]
    return res
n = int(input())
a = list(map(int, input().split()))

if __name__ == '__main__':
    f()