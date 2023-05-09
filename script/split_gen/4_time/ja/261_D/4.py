def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    c = []
    y = []
    for i in range(m):
        ci, yi = map(int, input().split())
        c.append(ci)
        y.append(yi)
    # print(n, m)
    # print(x)
    # print(c)
    # print(y)
    ans = 0
    for i in range(n):
        ans += x[i]
        for j in range(m):
            if i+1 == c[j]:
                ans += y[j]
    print(ans)
