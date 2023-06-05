def main():
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    #print(a)
    res = 0
    if k*x > a[-1]:
        res = a[-1]
    else:
        res = k*x
    for i in range(n-1):
        res += a[i]
    print(res)
