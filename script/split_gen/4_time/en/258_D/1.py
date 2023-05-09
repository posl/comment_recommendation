def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    ans = 10**18
    for i in range(n):
        tmp = x * a[i] + b[i] * (n - x)
        if ans > tmp:
            ans = tmp
    print(ans)
